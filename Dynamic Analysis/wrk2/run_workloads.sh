./wrk -D exp -t 2 -c 10 -d 100 -L -s ./scripts/media-microservices/compose-review.lua http://10.10.1.143:8080/wrk2-api/review/compose -R 2000 > ./results/mrm_runsc1.txt
./wrk -D exp -t 3 -c 10 -d 100 -L -s ./scripts/media-microservices/compose-review.lua http://10.10.1.143:8080/wrk2-api/review/compose -R 2000 > ./results/mrm_runsc2.txt
./wrk -D exp -t 4 -c 10 -d 100 -L -s ./scripts/media-microservices/compose-review.lua http://10.10.1.143:8080/wrk2-api/review/compose -R 2000 > ./results/mrm_runsc3.txt
./wrk -D exp -t 5 -c 10 -d 100 -L -s ./scripts/media-microservices/compose-review.lua http://10.10.1.143:8080/wrk2-api/review/compose -R 2000 > ./results/mrm_runsc4.txt
./wrk -D exp -t 5 -c 5  -d 100 -L -s ./scripts/media-microservices/compose-review.lua http://10.10.1.143:8080/wrk2-api/review/compose -R 2000 > ./results/mrm_runsc5.txt
./wrk -D exp -t 5 -c 15 -d 100 -L -s ./scripts/media-microservices/compose-review.lua http://10.10.1.143:8080/wrk2-api/review/compose -R 2000 > ./results/mrm_runsc6.txt
./wrk -D exp -t 5 -c 20 -d 100 -L -s ./scripts/media-microservices/compose-review.lua http://10.10.1.143:8080/wrk2-api/review/compose -R 2000 > ./results/mrm_runsc7.txt
./wrk -D exp -t 5 -c 10 -d 100 -L -s ./scripts/media-microservices/compose-review.lua http://10.10.1.143:8080/wrk2-api/review/compose -R 2500 > ./results/mrm_runsc8.txt
./wrk -D exp -t 5 -c 10 -d 100 -L -s ./scripts/media-microservices/compose-review.lua http://10.10.1.143:8080/wrk2-api/review/compose -R 1500 > ./results/mrm_runsc9.txt
./wrk -D exp -t 5 -c 10 -d 100 -L -s ./scripts/media-microservices/compose-review.lua http://10.10.1.143:8080/wrk2-api/review/compose -R 750 > ./results/mrm_runsc10.txt