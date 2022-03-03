# tried only for images that exist
# does not try and catch any errors of failures
import os
import re
path = "./pmap/"
files_list = []
for i,j,k in os.walk(path):
    files_list.extend(k)
for name in files_list:
    f = open(path+name,'r')
    x = f.readlines()
    f.close()
    if len(x)!=0:
        for i in x:
            if ('[' not in i) and ('/' in i):
                i = i.split(' ')[-1][:-1]
                cmd = "docker exec -it "+name[:-4]+" dpkg -S "+i+" >> libraries_needed/"+name
                os.system(cmd)
    print(name[:-4],"done")
    print("---------------------")