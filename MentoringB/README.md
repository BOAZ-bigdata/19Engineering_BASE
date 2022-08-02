# How to run~

## Prerequisites
- Docker
- Python3

## Steps

### Server
0. cd socker-server
1. docker build -t { image_name } .
2. docker run -t -p { port }:{ port } --name { user } --rm { image_name }
- this terminal will be your acting server

### Client
0. open another termianl
1. cd socket-client
2. python3 client.py
- this terminal will be your local client

