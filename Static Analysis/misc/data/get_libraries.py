# tried only for images that exist
# does not try and catch any errors of failures
import os
import re
path = "./full_path/so_files/"
files_list = []
for i,j,k in os.walk(path):
    files_list.extend(k)
for name in files_list:
    f = open(path+name,'r')
    x = f.readlines()
    if len(x)!=0:
        for i in x:
            if '\n' in i:
                i = i[:-1]
            cmd = "docker exec -it dockercomposemanifests_ts-"+name[:-4]+"_1 dpkg -S "+i+" >> libraries_used/"+name
            os.system(cmd)
    print(name[:-4],"done")
    print("---------------------")