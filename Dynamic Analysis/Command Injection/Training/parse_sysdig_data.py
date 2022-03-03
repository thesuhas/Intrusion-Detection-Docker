from datetime import datetime,timedelta

syscalls = dict()
# Syscall has integer for each syscall
with open('syscall.csv') as f:
    for line in f:
        n,s = line.split(',')
        n = int(n)
        s = s.strip()
        syscalls[s] = n

# Mapping of input to output directories
x = {'Data/normal_workload.txt':'./Dataset/Normal/Normal','Data/attack_workload.txt':'./Dataset/Attack/Attack'}
for workload_type in x:
    current_time = None
    current_count = 1
    # Open the worload file
    with open(workload_type) as f:
        for line in f:
            t,s = line.split(' ')
            s = s.strip()
            # If the given syscall is not in the list of syscalls
            if s not in syscalls:
                continue
            # Remove last 3 digits of time
            t = t[:-3]
            # Convert to datetime object of appropriate format
            dt = datetime.strptime(t,"%H:%M:%S.%f")
            # Get syscall integer
            sn = syscalls[s]
            if current_time is None:
                current_time = dt
                # Create file to write data to
                ft = open(x[workload_type]+str(current_count)+'.txt','a+')
            # Write system calls as long as 100ms are not up
            if dt - current_time < timedelta(milliseconds=100):
                ft.write(str(sn)+" ")
            # Stop writing to file as 100ms are done
            else:
                ft.close()
                current_count += 1
                current_time = dt
                # Open next file
                ft = open(x[workload_type]+str(current_count)+'.txt','a+')
