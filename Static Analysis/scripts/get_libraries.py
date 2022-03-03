# tried only for images that exist
# does not try and catch any errors of failures
import os
import re
path = "./pmap/"
files_list = []
# Returns roots, directories and files from location `path`
# Directory is scanned from top-down (includes all subdirectories as well)
for i,j,k in os.walk(path):
    # Adds files in directory to end of `files_list`
    files_list.extend(k)
for name in files_list:
    f = open(path+name,'r')
    x = f.readlines()
    f.close()
    res = set()
    if len(x)!=0:
        for i in x:
            # Adds processes that have a definitive file mapping
            # Does not add `anon` mapping, i.e., mapping not backed by a file (could have been created via malloc or mmap)
            if ('[' not in i) and ('/' in i):
                res.add(i.split(' ')[-1][:-1])
    for i in res:
        # Runs a command in docker container
        cmd = "docker exec -it "+name[:-4]+" dpkg -S "+i+" >> libraries_needed/"+name
        os.system(cmd)
    print(name[:-4],"done")
    print("---------------------")