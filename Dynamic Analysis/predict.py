import pickle
import pandas as pd
import threading
import os
from sklearn import svm
from sklearn import metrics
from sklearn.model_selection import train_test_split
from collections import OrderedDict
import time
from collections import defaultdict

from datetime import datetime,timedelta

syscalls = dict()
with open('syscall.csv') as f:
    for line in f:
        n,s = line.split(',')
        n = int(n)
        s = s.strip()
        syscalls[s] = n

filename = 'finalized_model_svm.sav'
loaded_model = pickle.load(open(filename, 'rb'))

# Load syscalls data into a dictionary
syscalls = dict()
with open('syscall.csv') as f:
    for line in f:
        n,s = line.split(',')
        n = int(n)
        s = s.strip()
        syscalls[s] = n

# Creates a vector of all the system calls
columns = [j for i,j in syscalls.items()]
current_time = None

a='Attack'
n='Normal'
vec_type = int(input('enter 0 for normal, 1 for attack'))
fn = a if vec_type==1 else n
suffix = input('enter suffix digit')
f = open("./Training/complete_vector/"+fn+suffix+".txt","r")
l = f.readlines()
f.close()

# Function for prediction
def predict(freq, columns):
    # Create dataframe with required columns
    df_res = pd.DataFrame(columns=columns)
    # Add syscall frequency to respective columns
    df_res =  df_res.append(freq, ignore_index=True)
    # Fill non-occuring syscalls with 0
    df_res = df_res.fillna(0)
    # Give DF to model to predict
    res = loaded_model.predict(df_res)
    # Printing thread
    print(f"Thread {threading.current_thread().name}")
    # print(res)
    if res[0] == 1:
        print(count,"\tATTACK DETECTED")
        print(freq)
    else:
        print(count, "\tNo attack")
        print(freq)

freq = dict()
count=1
current_time = None
columns = [j for i,j in syscalls.items()]
for line in l:
    # print('>>> {}'.format(line.decode('utf-8').rstrip()))
    # print(line.decode('utf-8').rstrip().split(' '))
    # t,s = line.decode('utf-8').strip('"|\n').split(' ')
    # t,s = line.strip('"|\n').split(' ')
    # s = s.strip()
    line = line.rstrip()
    # print(line)
    t,s = line.split(' ')
    # print(t,s)    

    # T is time, s is syscall
    s = s.strip()
    if s not in syscalls:
        continue
    t = t[:-3]
    # Time of call being executed
    dt = datetime.strptime(t,"%H:%M:%S.%f")
    sn = syscalls[s]
    # If first pass, get current time
    if current_time is None:
        current_time = dt
    # If 100ms has not elapsed
    if dt - current_time < timedelta(milliseconds=100):
        if sn not in freq:
            freq[sn] = 0
        # Add frequency of the system call
        freq[sn] += 1
    # If 100 seconds has elapsed
    else:
        # Create thread and start as required
        threading.Thread(target=predict, args=(freq, columns,)).start()
        current_time = dt
        # print(freq)
        # print(df_res)
        freq.clear()
        count += 1