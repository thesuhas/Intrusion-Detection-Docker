import shutil
import subprocess
import sys
import argparse
import threading
import requests
import os
import datetime

def thread_func(dest_addr, payload):
    requests.post(dest_addr, json={'IP': payload})

def clean_file(filename: str):
    
    
    og = filename
    # if there are any spaces in the filename, we need to escape it
    filepath = filename.split('/')[:-1]
    filepath = '/'.join(filepath)
    dup = f'{filepath}/copy.txt'
    # copy the file to a new file
    shutil.copy(og, dup)

    # remove lines that are not in the list above
    with open(dup, 'r') as f:
        lines = f.readlines()
    with open(dup, 'w') as f:
        for line in lines:
            if line.split(' ')[1] in syscalls:
                f.write(line)
    # prompt the user for whenever sysdig is killed
    input('Press enter to continue after killing sysdig')
    # remove original file
    os.remove(og)
    # rename copy to original
    os.rename(dup, og)
syscalls = [
        'read',
        'write',
        'open',
        'close',
        'stat',
        'fstat',
        'lstat',
        'poll',
        'lseek',
        'mmap',
        'mprotect',
        'munmap',
        'brk',
        'rt_sigaction',
        'rt_sigprocmask',
        'rt_sigreturn',
        'ioctl',
        'pread64',
        'pwrite64',
        'readv',
        'writev',
        'access',
        'pipe',
        'select',
        'sched_yield',
        'mremap',
        'msync',
        'mincore',
        'madvise',
        'shmget',
        'shmat',
        'shmctl',
        'dup',
        'dup2',
        'pause',
        'nanosleep',
        'getitimer',
        'alarm',
        'setitimer',
        'getpid',
        'sendfile',
        'socket',
        'connect',
        'accept',
        'sendto',
        'recvfrom',
        'sendmsg',
        'recvmsg',
        'shutdown',
        'bind',
        'listen',
        'getsockname',
        'getpeername',
        'socketpair',
        'setsockopt',
        'getsockopt',
        'clone',
        'fork',
        'vfork',
        'execve',
        'exit',
        'wait4',
        'kill',
        'uname',
        'semget',
        'semop',
        'semctl',
        'shmdt',
        'msgget',
        'msgsnd',
        'msgrcv',
        'msgctl',
        'fcntl',
        'flock',
        'fsync',
        'fdatasync',
        'truncate',
        'ftruncate',
        'getdents',
        'getcwd',
        'chdir',
        'fchdir',
        'rename',
        'mkdir',
        'rmdir',
        'creat',
        'link',
        'unlink',
        'symlink',
        'readlink',
        'chmod',
        'fchmod',
        'chown',
        'fchown',
        'lchown',
        'umask',
        'gettimeofday',
        'getrlimit',
        'getrusage',
        'sysinfo',
        'times',
        'ptrace',
        'getuid',
        'syslog',
        'getgid',
        'setuid',
        'setgid',
        'geteuid',
        'getegid',
        'setpgid',
        'getppid',
        'getpgrp',
        'setsid',
        'setreuid',
        'setregid',
        'getgroups',
        'setgroups',
        'setresuid',
        'getresuid',
        'setresgid',
        'getresgid',
        'getpgid',
        'setfsuid',
        'setfsgid',
        'getsid',
        'capget',
        'capset',
        'rt_sigpending',
        'rt_sigtimedwait',
        'rt_sigqueueinfo',
        'rt_sigsuspend',
        'sigaltstack',
        'utime',
        'mknod',
        'uselib',
        'personality',
        'ustat',
        'statfs',
        'fstatfs',
        'sysfs',
        'getpriority',
        'setpriority',
        'sched_setparam',
        'sched_getparam',
        'sched_setscheduler',
        'sched_getscheduler',
        'sched_get_priority_max',
        'sched_get_priority_min',
        'sched_rr_get_interval',
        'mlock',
        'munlock',
        'mlockall',
        'munlockall',
        'vhangup',
        'modify_ldt',
        'pivot_root',
        '_sysctl',
        'prctl',
        'arch_prctl',
        'adjtimex',
        'setrlimit',
        'chroot',
        'sync',
        'acct',
        'settimeofday',
        'mount',
        'umount2',
        'swapon',
        'swapoff',
        'reboot',
        'sethostname',
        'setdomainname',
        'iopl',
        'ioperm',
        'create_module',
        'init_module',
        'delete_module',
        'get_kernel_syms',
        'query_module',
        'quotactl',
        'nfsservctl',
        'getpmsg',
        'putpmsg',
        'afs_syscall',
        'tuxcall',
        'security',
        'gettid',
        'readahead',
        'setxattr',
        'lsetxattr',
        'fsetxattr',
        'getxattr',
        'lgetxattr',
        'fgetxattr',
        'listxattr',
        'llistxattr',
        'flistxattr',
        'removexattr',
        'lremovexattr',
        'fremovexattr',
        'tkill',
        'time',
        'futex',
        'sched_setaffinity',
        'sched_getaffinity',
        'set_thread_area',
        'io_setup',
        'io_destroy',
        'io_getevents',
        'io_submit',
        'io_cancel',
        'get_thread_area',
        'lookup_dcookie',
        'epoll_create',
        'epoll_ctl_old',
        'epoll_wait_old',
        'remap_file_pages',
        'getdents64',
        'set_tid_address',
        'restart_syscall',
        'semtimedop',
        'fadvise64',
        'timer_create',
        'timer_settime',
        'timer_gettime',
        'timer_getoverrun',
        'timer_delete',
        'clock_settime',
        'clock_gettime',
        'clock_getres',
        'clock_nanosleep',
        'exit_group',
        'epoll_wait',
        'epoll_ctl',
        'tgkill',
        'utimes',
        'vserver',
        'mbind',
        'set_mempolicy',
        'get_mempolicy',
        'mq_open',
        'mq_unlink',
        'mq_timedsend',
        'mq_timedreceive',
        'mq_notify',
        'mq_getsetattr',
        'kexec_load',
        'waitid',
        'add_key',
        'request_key',
        'keyctl',
        'ioprio_set',
        'ioprio_get',
        'inotify_init',
        'inotify_add_watch',
        'inotify_rm_watch',
        'migrate_pages',
        'openat',
        'mkdirat',
        'mknodat',
        'fchownat',
        'futimesat',
        'newfstatat',
        'unlinkat',
        'renameat',
        'linkat',
        'symlinkat',
        'readlinkat',
        'fchmodat',
        'faccessat',
        'pselect6',
        'ppoll',
        'unshare',
        'set_robust_list',
        'get_robust_list',
        'splice',
        'tee',
        'sync_file_range',
        'vmsplice',
        'move_pages',
        'utimensat',
        'epoll_pwait',
        'signalfd',
        'timerfd_create',
        'eventfd',
        'fallocate',
        'timerfd_settime',
        'timerfd_gettime',
        'accept4',
        'signalfd4',
        'eventfd2',
        'epoll_create1',
        'dup3',
        'pipe2',
        'inotify_init1',
        'preadv',
        'pwritev',
        'rt_tgsigqueueinfo',
        'perf_event_open',
        'recvmmsg',
        'fanotify_init',
        'fanotify_mark',
        'prlimit64',
        'name_to_handle_at',
        'open_by_handle_at',
        'clock_adjtime',
        'syncfs',
        'sendmmsg',
        'setns',
        'getcpu',
        'process_vm_readv',
        'process_vm_writev',
        'kcmp',
        'finit_module',
        'sched_setattr',
        'sched_getattr',
        'renameat2',
        'seccomp',
        'getrandom',
        'memfd_create',
        'kexec_file_load',
        'bpf',
        'execveat',
        'userfaultfd',
        'membarrier',
        'mlock2',
        'copy_file_range',
        'preadv2',
        'pwritev2',
        'pkey_mprotect',
        'pkey_alloc',
        'pkey_free',
        'statx'
    ]
parser = argparse.ArgumentParser(description='Collect data from a vulnerable app.')
parser.add_argument('-c', '--container', type=str, default='ping', help='The name of the container. Default is ping.')
parser.add_argument('-w', '--workload', type=str, default='normal', help='The type of workload. Default is normal.')

args = parser.parse_args()
container = args.container
workload = args.workload

if container not in ['ping', 'sqli']:
    print('Invalid container name.')
    print('Please use one of the following: ping, sqli.')
    sys.exit(1)

if workload not in ['normal', 'attack']:
    print('Wrong workload type!')
    sys.exit(1)

if container == 'ping':
    print('Collecting data from ping container...')
    dest_dir = './commandInjection/Training'
    dest_addr = 'http://localhost:8081/api/ping'
    if workload == 'normal':
        print("Normal workload")
        filename = 'normal_workload.txt'
        payload = input('Please input the IP of the target:\n')
    else:
        print("Attack workload")
        type_of_attack = input('Please input the type of attack:\n').replace(' ', '_')
        payload = input('Please input the attack workload without any next line characters:\n')
        filename = f'attack_{type_of_attack}_workload.txt'
    # sysdig_cmd = f'sudo sysdig -p "%evt.time %evt.type %evt.args" container.name=ping_container > "{dest_dir}/sysdig_data/{filename}"'
    sysdig_cmd = ['sudo', 'sysdig', '-p', '"%evt.time %syscall.type %container.mounts %proc.args %proc.nthreads %proc.nchilds %proc.fdopencount %proc.vmsize %evt.args"', 'container.name=ping_container']
    run = subprocess.Popen(sysdig_cmd, stdout=subprocess.PIPE)
    fp = open(f"{dest_dir}/sysdig_data/{filename}", 'w')
    print("Process ID of sysdig:", run.pid + 1)
    print(f"Get ready to run this:\nsudo kill {run.pid + 1}")
    t1 = threading.Thread(target=thread_func, args=(dest_addr, payload)).start()
    # res = requests.post(dest_addr, json={'IP': payload})
    for line in iter(run.stdout.readline, b''):
        line = line.decode('utf-8').strip().replace('"', '')
        syscall = line.split(' ')[1].strip()
        
        if(syscall in syscalls):
            # print(syscall)
            fp.write(line.strip() + '\n')
            if(syscall == 'exit'):
                print('exit')
                break
    ls = os.popen('ls -l /proc/self/fd').read()
    print(ls)
    print("Kill sysdig now!")
    fp.close()
    os.popen(f'sudo kill {run.pid + 1}')
    now = datetime.datetime.now().strftime('%H:%M:%S.%f')
    print(now)
    print("Kill sysdig now!")
    run.kill()
    os.system(f'sudo kill {run.pid + 1}')
    # clean_path = os.path.join(os.getcwd(), 'commandInjection', 'Training', 'sysdig_data', filename)
    # clean_file(clean_path)

else:
    dest_dir = './sqli/Training/'
    dest_addr = 'http://localhost:8082/api/sqli'
    if workload == 'normal':
        filename = 'normal_workload.txt'
    else:
        type_of_attack = input('Please input the type of attack:\n').replace(' ', '_')
        attack_workload = input('Please input the attack workload without any next line characters:\n')
        filename = f'attack_{type_of_attack}_workload.txt'
    print("Still under dev")
