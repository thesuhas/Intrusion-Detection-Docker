#
# MOVE FILE OUTSIDE DATASET DIRECTORY
#

from collections import Counter

import os
import pandas as pd
import numpy as np
types = ['Normal','Attack']
for i in types:
    directory = os.path.join('.', 'Dataset',i)
    try:
        for root, dirs, files in os.walk(directory, topdown=False):
            for name in files:
                path = os.path.join(root, name)
                # print(path)
                with open(path, 'r') as f:
                    s = f.read()
                seq = s.strip().split(" ")
                if len(seq) < 15:
                    continue
                # try:
                #     seq = list(map(int, seq))
                # except ValueError:
                #     print("Error",seq,path)
                #     continue
                count = Counter(seq)   
                df = pd.DataFrame.from_dict(count, orient='index').reset_index()
                df = df.rename(columns={'index':'syscall', 0:'count'})
                new_name = name.strip('txt') + 'csv'
                csv_path = os.path.join(root,'csv', new_name)
                # print(csv_path)
                df.to_csv(csv_path, index=False)
    except:
        pass

