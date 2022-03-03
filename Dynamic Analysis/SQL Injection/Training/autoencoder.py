from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import pandas as pd
import os
import csv
from glob import glob
import sklearn
from sklearn import metrics
from sklearn.model_selection import train_test_split
import time
import matplotlib.pyplot as plt 
from sklearn.metrics import plot_confusion_matrix

# This is the size of our encoded representations
encoding_dim = 33  # 32 floats -> compression of factor 24.5, assuming the input is 784 floats

# This is our input image
input_img = keras.Input(shape=(332,))
# "encoded" is the encoded representation of the input
encoded = layers.Dense(encoding_dim, activation='relu')(input_img)
# "decoded" is the lossy reconstruction of the input
decoded = layers.Dense(332, activation='sigmoid')(encoded)

# This model maps an input to its reconstruction
autoencoder = keras.Model(input_img, decoded)

# This model maps an input to its encoded representation
encoder = keras.Model(input_img, encoded)

# This is our encoded (32-dimensional) input
encoded_input = keras.Input(shape=(encoding_dim,))
# Retrieve the last layer of the autoencoder model
decoder_layer = autoencoder.layers[-1]
# Create the decoder model
decoder = keras.Model(encoded_input, decoder_layer(encoded_input))

autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

PATH = "./Dataset/Normal"
EXT = "*.csv"
all_csv_files = [file
                 for path, subdir, files in os.walk(PATH)
                 for file in glob(os.path.join(path, EXT))]

df = pd.DataFrame()
for name in all_csv_files:
    ground_truth = 0
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
y = df['Truth']
df = df.drop(columns=[4,"Truth"])

X_train, X_test, Y_train, Y_test = train_test_split(df, y, test_size=0.3)
print("X_train.shape:", X_train.shape)
print("X_test.shape:", X_test.shape)

autoencoder.fit(X_train, X_train,
                epochs=10,
                batch_size=256,
                shuffle=True)

# # Encode and decode some digits
# # Note that we take them from the *test* set
encoded_imgs = encoder.predict(X_train)
decoded_imgs = decoder.predict(encoded_imgs)

a = np.power(X_train - decoded_imgs, 2)
mse = np.mean(a, axis=1)
mse_max = max(mse)

print("power : ",a)
with open("mse.txt","w") as f:
    for i in mse:
        print(i,file=f)
print(type(mse))

PATH = "./Dataset/Attack"
EXT = "*.csv"
all_csv_files = [file
                 for path, subdir, files in os.walk(PATH)
                 for file in glob(os.path.join(path, EXT))]

df2 = pd.DataFrame()
for name in all_csv_files:
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
    df2 =  df2.append(new_dict, ignore_index=True)

for i in range(333):
    if i not in df2:
        df2[i] = [0 for j in range(len(df2))]
df2 = df2.fillna(0)
df2 = df2.sample(frac=1)
y = df2['Truth']
df2 = df2.drop(columns=[4,"Truth"])

X_a_train, X_a_test, Y_a_train, Y_a_test = train_test_split(df2, y, test_size=0.3)


X_final_test = np.append(X_test, X_a_test, axis=0)
Y_final_test = np.append(Y_test, Y_a_test, axis=0)


encoded_imgs = encoder.predict(X_a_test)
decoded_imgs = decoder.predict(encoded_imgs)

y_pred = []
a = np.power(X_a_test - decoded_imgs, 2)
mse = np.mean(a, axis=1)
for i in mse:
    print(i)
    if i > mse_max:
        y_pred.append(1)
    else:
        y_pred.append(0)
y_pred = np.array(y_pred)


# print("is x, xa, x_final nan:", np.isnan(X_test).any(), np.isnan(X_a_test).any(), np.isnan(X_final_test).any())
# print("shapes of Xs (add):", X_final_test.shape, X_test.shape, X_a_test.shape)
# print("is y, ya, y_final, y_pred nan:", np.isnan(Y_test).any(), np.isnan(Y_a_test).any(), np.isnan(Y_final_test).any(), np.isnan(y_pred).any())
# print("shape of ys (scores) are equal:", Y_final_test.shape == y_pred.shape)

print("Accuracy:",metrics.accuracy_score(Y_a_test, y_pred))
print("Precision:",metrics.precision_score(Y_a_test, y_pred))
print("Recall:",metrics.recall_score(Y_a_test, y_pred))
