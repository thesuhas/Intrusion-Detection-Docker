from dtw import *

# Import first and second file

file1 = open('./parsed_sysdig_data/attack_mounted_socket_1_workload_parsed.txt', 'r')
file2 = open('./parsed_sysdig_data/attack_process_injection_1_workload_parsed.txt', 'r')

f1 = list()
for line in file1:
    f1.append(line.split(',')[1])

f2 = list()
for line in file2:
    f2.append(line.split(',')[1])

alignment = dtw(f1, f2, keep_internals=True)

alignment.plot(type='threeway')