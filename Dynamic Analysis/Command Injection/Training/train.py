import pandas as pd
import os
import csv
from glob import glob
import sklearn
from sklearn import svm
from sklearn import metrics
from sklearn.model_selection import train_test_split
import pickle
import time
import matplotlib.pyplot as plt 
from sklearn.metrics import plot_confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler



PATH = "./Dataset/"
EXT = "*.csv"
# Gets list of all csv files to iterate through
all_csv_files = [file
                 for path, subdir, files in os.walk(PATH)
                 for file in glob(os.path.join(path, EXT))]

print(all_csv_files[:10])
print(len(all_csv_files))


df = pd.DataFrame()
for name in all_csv_files:
    # Get class label for each file
    ground_truth = 0
    if '/Norm' in name:
        ground_truth = 0
    elif '/Atta' in name:
        ground_truth = 1
    # Create csv
    df1 = pd.read_csv(name)
    new_dict = dict()
    try:
        for index, row in df1.iterrows():
            #print(row['syscall'], row['count'])

            # Add (syscall, count) entry to dict
            new_dict[row['syscall']] = row['count']
    except:
        print(name)
        raise KeyError

    # Get whether vector is attack or normal
    new_dict['Truth'] = ground_truth
    # Add to dataframe
    df =  df.append(new_dict, ignore_index=True)

# why 333? 
for i in range(333):
    if i not in df:
        df[i] = [0 for j in range(len(df))]

# Filling missing values
df = df.fillna(0)
# Shuffles the dataframe and returns rows in random order
df = df.sample(frac=1)

print("len", len(df.columns))
# X_with_4 = df.loc[:, df.columns != 'Truth']
X = df.drop(columns=["Truth"])
y = df['Truth']

# Create new scaler
stdScaler = StandardScaler()
X = stdScaler.fit_transform(X)
X = pd.DataFrame(X)
#print(X)

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.25, random_state=1, stratify=y)

# Run gridsearch to get best params
# params = {
#     'kernel': ['linear', 'rbf', 'sigmoid'], 
#     'C': [0.001, 0.05, 0.01, 0.1, 1, 5, 10, 100], 
#     'gamma': [0.01, 0.1, 1, 5, 10, 100]
#     }
# gs = GridSearchCV(estimator=svm.SVC(), param_grid=params, n_jobs=-1, verbose=3)
# gs.fit(X_train, Y_train)
# print(gs.best_params_)
# print(gs.best_score_)
clf = svm.SVC(kernel='linear', gamma=0.01, C=0.05)

now = time.time()
clf.fit(X_train, Y_train)
total = time.time() - now

y_pred = clf.predict(X_test)

print("Accuracy:",metrics.accuracy_score(Y_test, y_pred))
print("Precision:",metrics.precision_score(Y_test, y_pred))
print("Recall:",metrics.recall_score(Y_test, y_pred))
print("F1 Score:", metrics.f1_score(Y_test, y_pred))
print("Time to Train:",total * 1000)

filename = '../finalized_model_pers.sav'
pickle.dump(clf, open(filename, 'wb'))


plot_confusion_matrix(clf, X_test, Y_test) 
plt.savefig("../mygraph.png")