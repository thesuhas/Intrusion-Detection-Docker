FROM ubuntu
WORKDIR /app
EXPOSE 8081
COPY requirements.txt /app
# Install any needed packages specified in requirements.txt
RUN apt-get update -y && \
    apt-get install -y python3-pip iputils-ping
RUN pip3 install -r requirements.txt
COPY app.py /app
CMD python3 app.py
