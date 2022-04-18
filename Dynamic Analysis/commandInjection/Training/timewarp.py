from mmap import MADV_NOHUGEPAGE
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean
import numpy as np
import os
import pandas as pd

# Import first and second file



def dtw(file1, file2):

    file1 = open(file1, 'r')
    file2 = open(file2, 'r')

    f1 = list()
    for line in file1:
        f1.append(np.double(line.split(',')[1]))
        

    f2 = list()
    for line in file2:
        f2.append(np.double(line.split(',')[1]))

    f1 = np.array(f1)
    f2 = np.array(f2)
    # print(type(f1[0]))
    print(f1, f2)
    # print("path started")
    distance, path = fastdtw(f1, f2, dist=euclidean)
    # print("path done")
    return distance
    

if __name__ == "__main__":

    path = os.path.join(os.getcwd(), 'parsed_sysdig_data')

    print("Starting Dynamic Time Warping")
    mounted_socket = []
    process_injection = []
    for x in os.listdir(path):
        if x.startswith('attack_mounted_socket'):
            mounted_socket.append(x)
        elif x.startswith('attack_process_injection'):
            process_injection.append(x)

    df = pd.DataFrame()

    for f1 in mounted_socket:
        for f2 in process_injection:
            print(f1, f2)
            distance = dtw(file1=os.path.join(path, f1), file2=os.path.join(path, f2))
            result = {
                'f1': f1,
                'f2': f2,
                'dist': distance
            }
            df = df.append(result, ignore_index=True)
            
    df.to_csv('dtw_mountedSocket_processInjection.csv')
    print("Written DF to disk")
