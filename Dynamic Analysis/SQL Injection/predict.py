import pickle
import pandas as pd
import os
from sklearn import svm
from sklearn import metrics
from sklearn.model_selection import train_test_split
from collections import OrderedDict
import time


filename = 'finalized_model_pers.sav'
 
# columns = [ 0,  1,  2,  3,  4,  5,  7,  8,
#    9, 10, 11, 12, 13, 14, 16, 21,
#   22, 32, 39, 41, 42, 43, 44, 45,
#   47, 51, 54, 55, 56, 59, 61, 79,
#   89,102,104,105,107,108,110,125,
#  126,157,158,186,202,217,257,269,
#  273, 38, 63, 72, 83, 87, 91,
#   95, 99,111,137,218,221,230,231,
#  268, 28, 48, 60, 24, 23]
columns = list(range(332))
# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))

df_res = pd.DataFrame(columns=columns)
# df_res = df_res.loc[:, df_res.columns != 'Truth']

fileno = input("enter file number")
df_test = pd.read_csv('./Training/Dataset/Attack2/csv/Attack' + fileno + '.csv')
# for root, dirs, files in os.walk("../Dataset/Attack2/csv/"):
#     for filename in files:
# df_test = pd.read_csv("../Dataset/Attack2/csv/Attack" + fileno)
# print("testing file", fileno)
new_dict = dict()
try:
    for index, row in df_test.iterrows():
        new_dict[row['syscall']] = row['count']
        #print(row['syscall'], row['count'])
except:
    print(fileno)
    raise KeyError

df_res = pd.DataFrame(columns=columns)
df_res =  df_res.append(new_dict, ignore_index=True)
df_res = df_res.fillna(0)

# dict1 = OrderedDict(sorted(new_dict.items()))
# dict2 = dict(dict1)
# print(dict1)
# print(dict2)
# print(df_res)

res = loaded_model.predict(df_res)
# print(res)
if res[0] == 1:
    # pass
    print("ATTACK detected", fileno)
else:
    print("No attack", fileno)
# now = time.time()
# print(loaded_model.predict(df_res))
# total = time.time() - now
# print(total)

# import timeit
# exec_time = timeit.timeit(lambda: loaded_model.predict(df_res), number=10000)
# print(exec_time/(10000) * 1000)