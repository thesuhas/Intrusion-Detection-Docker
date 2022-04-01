from dtaidistance import dtw
from dtaidistance import dtw_visualisation as dtwvis
import numpy as np

# Import first and second file

file1 = open('./parsed_sysdig_data/attack_mounted_socket_1_workload_parsed.txt', 'r')
file2 = open('./parsed_sysdig_data/attack_mounted_socket_2_workload_parsed.txt', 'r')

f1 = list()
for line in file1:
    f1.append(int(line.split(',')[1]))
    

f2 = list()
for line in file2:
    f2.append(int(line.split(',')[1]))

f1 = np.array(f1)
f2 = np.array(f2)
# print(type(f1[0]))
path = dtw.warping_path(f1, f2)

dtwvis.plot_warping(f1, f2, path, filename='test1.png')