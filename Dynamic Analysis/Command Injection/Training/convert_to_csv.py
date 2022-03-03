#
# MOVE FILE OUTSIDE DATASET DIRECTORY
#

from collections import Counter

import os
import pandas as pd
import numpy as np
types = ['Normal','Attack']
for i in types:
    # Take into account both directories
    directory = os.path.join('.', 'Dataset',i)
    # try:
        # For all the files in the given directories
    for root, dirs, files in os.walk(directory, topdown=False):
        for name in files:
            path = os.path.join(root, name)
            # print(path)
            # Read the data
            with open(path, 'r') as f:
                s = f.read()
            # Get list of sys calls
            seq = s.strip().split(" ")
            # Don't do anything if less than 15 syscalls
            if len(seq) < 15:
                continue
            # try:
            #     seq = list(map(int, seq))
            # except ValueError:
            #     print("Error",seq,path)
            #     continue
            
            # Counts the number of instances of each item in the sequence
            count = Counter(seq)   
            # Create dataframe from resulting dict
            df = pd.DataFrame.from_dict(count, orient='index').reset_index()
            df = df.rename(columns={'index':'syscall', 0:'count'})
            new_name = name.strip('txt') + 'csv'
            csv_path = os.path.join(root,'csv', new_name)
            # print(csv_path)
            print(csv_path)
            df.to_csv(csv_path, index=False)
    # except:
    #     pass