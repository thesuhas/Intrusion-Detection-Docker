./wrk -D exp -t 2 -c 10 -d 100 -L -s ./scripts/media-microservices/compose-review.lua http://10.10.1.143:8080/wrk2-api/review/compose -R 2000 > ./res_first_layer_runsc/res1.txt
echo "."
./wrk -D exp -t 3 -c 10 -d 100 -L -s ./scripts/media-microservices/compose-review.lua http://10.10.1.143:8080/wrk2-api/review/compose -R 2000 > ./res_first_layer_runsc/res2.txt
echo "."
./wrk -D exp -t 4 -c 10 -d 100 -L -s ./scripts/media-microservices/compose-review.lua http://10.10.1.143:8080/wrk2-api/review/compose -R 2000 > ./res_first_layer_runsc/res3.txt
echo "."
./wrk -D exp -t 5 -c 10 -d 100 -L -s ./scripts/media-microservices/compose-review.lua http://10.10.1.143:8080/wrk2-api/review/compose -R 2000 > ./res_first_layer_runsc/res4.txt
echo "."
./wrk -D exp -t 5 -c 5  -d 100 -L -s ./scripts/media-microservices/compose-review.lua http://10.10.1.143:8080/wrk2-api/review/compose -R 2000 > ./res_first_layer_runsc/res5.txt
echo "."
./wrk -D exp -t 5 -c 15 -d 100 -L -s ./scripts/media-microservices/compose-review.lua http://10.10.1.143:8080/wrk2-api/review/compose -R 2000 > ./res_first_layer_runsc/res6.txt
echo "."
./wrk -D exp -t 5 -c 20 -d 100 -L -s ./scripts/media-microservices/compose-review.lua http://10.10.1.143:8080/wrk2-api/review/compose -R 2000 > ./res_first_layer_runsc/res7.txt
echo "."
./wrk -D exp -t 5 -c 10 -d 100 -L -s ./scripts/media-microservices/compose-review.lua http://10.10.1.143:8080/wrk2-api/review/compose -R 2500 > ./res_first_layer_runsc/res8.txt
echo "."
./wrk -D exp -t 5 -c 10 -d 100 -L -s ./scripts/media-microservices/compose-review.lua http://10.10.1.143:8080/wrk2-api/review/compose -R 1500 > ./res_first_layer_runsc/res9.txt
echo "."
./wrk -D exp -t 5 -c 10 -d 100 -L -s ./scripts/media-microservices/compose-review.lua http://10.10.1.143:8080/wrk2-api/review/compose -R 750 > ./res_first_layer_runsc/res10.txt
echo "."
