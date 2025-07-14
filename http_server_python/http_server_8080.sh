#!/bin/bash

python3 -m http.server 8080 > server.log 2>&1 & 

echo "Server started successfully: $(date +%Y_%m_%d_%H_%M_%S)" >> server.log
echo "listening on port 8080" >> server.log
echo >> server.log
echo >> server.log
echo "Start logging" >> server.log
cat server.log

