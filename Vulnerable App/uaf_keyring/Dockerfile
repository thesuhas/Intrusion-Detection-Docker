FROM Ubuntu:16.04

RUN apt update -y
RUN apt install gcc -y
RUN apt-get install libkeyutils-dev
COPY ./exploit /exploit
WORKDIR /exploit
RUN gcc 39277.c -o cve_2016_0728 -lkeyutils -Wall 

CMD ["./cve_2016_072 PP_KEY"]