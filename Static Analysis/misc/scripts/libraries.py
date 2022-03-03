import os
files_list = []
for i,j,k in os.walk("./libraries_needed/"):
    files_list.extend(k)
for name in files_list:
    f = open("./libraries_needed/"+name,'r')
    x = f.readlines()
    f.close()
    libs = set()
    for i in x:
        libs.add(i.split(':')[0])
    f = open("./libraries_needed/"+name,'a')
    print("\n----------------",file=f)
    for i in libs:
        print(i,file=f)
    f.close()