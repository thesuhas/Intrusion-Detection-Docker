import subprocess
import sys
import argparse
import requests
import os

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
    sysdig_cmd = f'sudo sysdig -p "%evt.time %evt.type" container.name=ping_container > "{dest_dir}/sysdig_data/{filename}"'
    run = subprocess.Popen(sysdig_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print("Process ID of sysdig:", run.pid + 1)
    print(f"Get ready to run this:\nsudo kill {run.pid + 1}")
    res = requests.post(dest_addr, json={'IP': payload})
    print("Response code:", res.status_code)
    print("Kill sysdig now!")
    subprocess.Popen(f'sudo kill {run.pid + 1}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    run.kill()

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
