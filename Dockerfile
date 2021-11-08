FROM ubuntu:18.04
EXPOSE 8005

RUN apt-get update && apt-get upgrade
RUN apt-get install python3.8 -y
RUN apt-get install python3-pip -y
RUN apt-get install git -y
RUN apt-get install curl -y
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3.8 get-pip.py
RUN git clone https://github.com/HeeGyoung/OpenBrewery.git
RUN pip3.8 install fastapi uvicorn requests
WORKDIR /OpenBrewery