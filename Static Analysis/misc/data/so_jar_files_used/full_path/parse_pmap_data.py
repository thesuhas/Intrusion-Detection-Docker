from os import walk
path_to_pmap_files = "pmap/"
files_list = []
for i,j,k in walk(path_to_pmap_files):
    files_list.extend(k)
for name in files_list:
    f = open(path_to_pmap_files+name,'r')
    print("---------")
    print(name)
    x = f.readlines()
    f.close()
    so_set = set()
    for i in x:
        if '[' not in i:
            if '/' in i:
                so_set.add(i.split(' ')[-1][:-1])
    op1 = open("files/"+name,'w')
    for i in so_set:
        print(i,file=op1)
    op1.close()
    print("Done\n---------")