#!/bin/bash
container_name=$1
if [ -z "$container_name" ]; then
    echo "Usage: $0 <container name> <type of workload>"
    exit 1
fi
type=$2
if [ -z "$type" ]; then
    echo "Usage: $0 <container name> <type of workload>"
    exit 1
fi
if [ "$type" != "normal" ] && [ "$type" != "attack" ]; then
    echo "Usage: $0 <container name> <type of workload>"
    exit 1
fi
if [ "$container_name" == "ping" ]; then
    dest_dir="commandInjection/Training"
    wrk_script="./wrk2/wrk -D exp -t 5 -c 10 -d 120 -L -s ./$dest_dir/workload_scripts/$type.lua http://localhost:8081/api/ping -R 1000"
elif [ "$container_name" == "sql" ]; then
    dest_dir="sqlInjection/Training"
    wrk_script="./wrk2/wrk -D exp -t 5 -c 10 -d 120 -L -s ./$dest_dir/workload_scripts/$type.lua http://localhost:8082/api/sqlquery -R 1000"
else 
    echo "Usage: $0 <container name> <type of workload>"
    echo "container name can only be ping or sql"
    exit 1
fi
sudo sysdig -p "%evt.time %evt.type" container.name=$container_name"_container" > "./$dest_dir/sysdig_data/${type}_workload.txt" &
pid=$!
echo 'Sysdig record has begun'
echo 'Workload will start now'
$wrk_script
echo 'Workload has finished'
echo $pid
sudo kill $pid
echo 'Sysdig record stopped'
echo 'fin.'
