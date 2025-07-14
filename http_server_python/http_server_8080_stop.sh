#!/bin/bash

stophttpserver=$(ps -aux | pgrep -f "python3 -m http.server 8080")

kill $stophttpserver && echo "processo terminato tramite script correttamente" >> server.log

mv ./server.log ./archive_log/server.log_$(date +%Y_%m_%d)_$stophttpserver

echo http.server has been stopped succesfully
