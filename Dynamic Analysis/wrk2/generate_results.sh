#!/bin/bash
while getopts ":f:" opt; do
  case $opt in
    f)
      mkdir $OPTARG
      ./wrk -D exp -t 2 -c 10 -d 100 -L -s ./scripts/media-microservices/compose-review.lua http://10.10.1.143:8080/wrk2-api/review/compose -R 2000 > $OPTARG/1.txt
      echo "1 done"
      ./wrk -D exp -t 3 -c 10 -d 100 -L -s ./scripts/media-microservices/compose-review.lua http://10.10.1.143:8080/wrk2-api/review/compose -R 2000 > $OPTARG/2.txt
      echo "2 done"
      ./wrk -D exp -t 4 -c 10 -d 100 -L -s ./scripts/media-microservices/compose-review.lua http://10.10.1.143:8080/wrk2-api/review/compose -R 2000 > $OPTARG/3.txt
      echo "3 done"
      ./wrk -D exp -t 5 -c 10 -d 100 -L -s ./scripts/media-microservices/compose-review.lua http://10.10.1.143:8080/wrk2-api/review/compose -R 2000 > $OPTARG/4.txt
      echo "4 done"
      ./wrk -D exp -t 5 -c 5  -d 100 -L -s ./scripts/media-microservices/compose-review.lua http://10.10.1.143:8080/wrk2-api/review/compose -R 2000 > $OPTARG/5.txt
      echo "5 done"
      ./wrk -D exp -t 5 -c 15 -d 100 -L -s ./scripts/media-microservices/compose-review.lua http://10.10.1.143:8080/wrk2-api/review/compose -R 2000 > $OPTARG/6.txt
      echo "6 done"
      ./wrk -D exp -t 5 -c 20 -d 100 -L -s ./scripts/media-microservices/compose-review.lua http://10.10.1.143:8080/wrk2-api/review/compose -R 2000 > $OPTARG/7.txt
      echo "7 done"
      ./wrk -D exp -t 5 -c 10 -d 100 -L -s ./scripts/media-microservices/compose-review.lua http://10.10.1.143:8080/wrk2-api/review/compose -R 2500 > $OPTARG/8.txt
      echo "8 done"
      ./wrk -D exp -t 5 -c 10 -d 100 -L -s ./scripts/media-microservices/compose-review.lua http://10.10.1.143:8080/wrk2-api/review/compose -R 1500 > $OPTARG/9.txt
      echo "9 done"
      ./wrk -D exp -t 5 -c 10 -d 100 -L -s ./scripts/media-microservices/compose-review.lua http://10.10.1.143:8080/wrk2-api/review/compose -R 750 > $OPTARG/10.txt
      echo "10 done"
      echo "All Tests Done. Results in "$OPTARG" folder"
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
done
      
