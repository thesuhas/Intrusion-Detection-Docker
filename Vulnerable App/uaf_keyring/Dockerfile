FROM ubuntu:14.04
WORKDIR /exploit

RUN apt update -y
RUN apt install gcc -y
RUN apt-get install libkeyutils-dev
COPY ./exploit /exploit
RUN gcc 39277.c -o cve_2016_0728 -lkeyutils -Wall 

CMD ["/bin/bash"]