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



PATH = "./Dataset/"
EXT = "*.csv"
all_csv_files = [file
                 for path, subdir, files in os.walk(PATH)
                 for file in glob(os.path.join(path, EXT))]

print(all_csv_files[:10])
print(len(all_csv_files))

df = pd.DataFrame()
for name in all_csv_files:
    ground_truth = 0
    if '/Norm' in name:
        ground_truth = 0
    elif '/Atta' in name:
        ground_truth = 1
    df1 = pd.read_csv(name)
    new_dict = dict()
    try:
        for index, row in df1.iterrows():
            #print(row['syscall'], row['count'])
            new_dict[row['syscall']] = row['count']
    except:
        print(name)
        raise KeyError


    new_dict['Truth'] = ground_truth
    df =  df.append(new_dict, ignore_index=True)

for i in range(333):
    if i not in df:
        df[i] = [0 for j in range(len(df))]
df = df.fillna(0)
df = df.sample(frac=1)

print("len", len(df.columns))
# X_with_4 = df.loc[:, df.columns != 'Truth']
X = df.drop(columns=["Truth"])
y = df['Truth']

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.25)

clf = svm.SVC(kernel='rbf')

now = time.time()
clf.fit(X_train, Y_train)
total = time.time() - now

y_pred = clf.predict(X_test)

print("Accuracy:",metrics.accuracy_score(Y_test, y_pred))
print("Precision:",metrics.precision_score(Y_test, y_pred))
print("Recall:",metrics.recall_score(Y_test, y_pred))
print("Time to Train:",total * 1000)

filename = '../finalized_model_pers.sav'
pickle.dump(clf, open(filename, 'wb'))


plot_confusion_matrix(clf, X_test, Y_test) 
plt.savefig("../mygraph.png")