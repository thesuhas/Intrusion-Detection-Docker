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
    if [ "$type" == "attack" ]; then
        type_of_attack=$3
        if [ -z "$type_of_attack" ]; then
            echo "Usage: $0 <container name> <type of workload> <type of attack> <workload script>"
            exit 1
        else 
            workload_script=$4
            if [ -z "$workload_script" ]; then
                echo "Usage: $0 <container name> <type of workload> <type of attack> <workload script>"
                exit 1
            else
                echo $workload_script
                curl_script="curl -s -X POST -H 'Content-Type: application/json' -d '{\"IP\":\"$workload_script\"}' http://localhost:8081/api/ping/"
                file_name=$type"_"$type_of_attack"_workload.txt"
                echo $curl_script
                echo $file_name
            fi
        fi
    else
        ip_address=$3
        if [ -z "$ip_address" ]; then
            echo "Usage: $0 <container name> <type of workload> <ip address>"
            exit 1
        else
            curl_script="curl -s -X POST -H 'Content-Type: application/json' -d '{\"IP\":\"$ip_address\"}' http://localhost:8081/api/ping/"
            file_name="normal_workload.txt"
            echo $curl_script
            echo $file_name
        fi
    fi
    dest_dir="commandInjection/Training"
elif [ "$container_name" == "sqli" ]; then
    dest_dir="sqlInjection/Training"
    echo "Still under dev."
    exit 1
else 
    echo "Usage: $0 <container name> <type of workload>"
    echo "container name can only be ping or sqli"
    exit 1
fi
sudo sysdig -p "%evt.time %evt.type" container.name=$container_name"_container" > "./$dest_dir/sysdig_data/$file_name" &
pid=$!
echo 'Sysdig record has begun'
echo 'Curl will start now'
$curl_script
echo 'Curl has finished'
echo $pid
sudo kill $pid
echo 'Sysdig record stopped'
echo 'fin.'
