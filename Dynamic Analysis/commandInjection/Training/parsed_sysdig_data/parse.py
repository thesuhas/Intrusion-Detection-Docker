import os

# Path of files to be parsed
path = os.path.join('..', 'sysdig_data')

# List of files
files = os.listdir(path)

# Extracting list of files with .txt extension
files = [f for f in files if f.endswith('.txt')]

# Loading syscall mapping
syscall = dict()

map_path = os.path.join('..', 'syscall.csv')

f = open(map_path, 'r')

for line in f:
    line = line.split(',')
    # :-1 strips newline character
    syscall[line[1][:-1]] = line[0]

# Parsing files

for file in files:
    f = open(os.path.join(path, file), 'r')

    # Opening output file
    out_path = os.path.join('..', 'parsed_sysdig_data', file[:-4]+'_parsed'+file[-4:])
    out_file = open(out_path, 'w')

    for line in f:
        line = line.split()

        # Extracting syscall name
        syscall_name = line[1]

        # Extracting time stamp
        timestamp = line[0][:-3]

        if syscall_name in syscall.keys():
            # Writing to output file
            out_file.write(timestamp + ',' + syscall[syscall_name] + '\n')

    # Closing output file
    out_file.close()