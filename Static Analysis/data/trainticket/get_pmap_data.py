import os
cmd = "docker-compose ps > container_names.txt"
os.system(cmd)
f = open("container_names.txt",'r')
x = f.readlines()
for i in x[2:]:
    n = i.split()[0]
    cmd = 'docker exec -it '+n+' sh -c "pmap -p 1" > pmap/'+n+'.txt'
    os.system(cmd)
print("pmap results saved in pmap folder")