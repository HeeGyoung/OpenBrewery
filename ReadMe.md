# API for Brewery

## Overview
This is an API to get brewery lists. 
To avoid some collisions within your local environment, this take-home task uses Docker on launch. 
Please follow the guide below.

## Development environment
* Language: Python3.8
* Framework: FastAPI(0.70.0)
* WSGI: uvicorn(0.15.0)
* Others: requests(2.26.0)  

All dependencies are automatically installed via Dockerfile.

## Install guide

### 1. Docker install
- [Link for mac](https://docs.docker.com/desktop/mac/install/)  
- [Link ror Windows](https://docs.docker.com/desktop/windows/install/)  
- [Link for others](https://docs.docker.com/engine/install/)

### 2. Execute shell script
```bash
chmod +x ./setup.sh
./setup.sh
```
By running this script, a docker image called "open brewery" will be created based on "Dockerfile" stating the CLI and other software we need. 
And then, the docker instance will be launched and executed API server with port number 8005.
Then, you can see the log from API server in your terminal.

### 3. Open your local website.
Open the URL below to review the API documentation and test the API.
```bash
http://127.0.0.1:8005/docs
```


### 4. Stop and remove
Press Ctrl+c to terminate Fastapi server.
To stop and eliminate the docker instance and image, copy and paste below commands. 
```bash
docker stop open_brewery
docker rm open_brewery
docker image rm open_brewery:0.1
```