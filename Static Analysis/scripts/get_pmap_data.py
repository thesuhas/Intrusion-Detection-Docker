import os
# Gets all running containers
cmd = "docker-compose ps > container_names.txt"
os.system(cmd)
f = open("container_names.txt",'r')
x = f.readlines()
for i in x[2:]:
    n = i.split()[0]
    # docker exec runs a command in a running container
    # Container the command is run is n
    # -it is used to run it in interactive mode, to bind input/output of host machine to that of container
    # https://stackoverflow.com/questions/30137135/confused-about-docker-t-option-to-allocate-a-pseudo-tty
    # Above link to properly understand -t option
    # sh is used to run default shell
    # -c is used to read commands from a string
    # -p is used to get the path of the mapping
    # PID 1 is the process that is responsible for starting and shutting down a container
    # Output of the command is stored in pmap/container.txt
    cmd = 'docker exec -it '+n+' sh -c "pmap -p 1" > pmap/'+n+'.txt'
    os.system(cmd)
print("pmap results saved in pmap folder")