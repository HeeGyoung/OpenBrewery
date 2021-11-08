# API for Brewery

## Overview

---

I made an API to get brewery lists.  
Just in case Curl/software that is needed to be installed makes some collisions in your local environment, I used docker.  
So, please follow the guide below.

---
## Install guide

### 1. Docker install
- [Link for mac](https://docs.docker.com/desktop/mac/install/)  
- [Link ror Windows](https://docs.docker.com/desktop/windows/install/)  
- [Link for others](https://docs.docker.com/engine/install/)

### 2. Excute shell script
```bash
bash setup.sh
```
In this script, the Curl/software that is needed is installed through Dockerfile.  
After that, the named "open_brewery" docker image will run with port number 8005.    

### 3. Turn on your local website.
```bash
http://127.0.0.1:8005/docs
```
Through this API document, you can use two types of API.

### 4. Stop and remove
First, stop container.
```bash
docker stop open_brewery
```
Second, remove container.
```bash
docker rm open_brewery
```
Third, remove image.
```bash
docker image rm open_brewery:0.1
```