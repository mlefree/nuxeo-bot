#!/bin/bash

#rm -rf .data
mkdir -p .data
IP=${IP:='127.0.0.1'}
echo "Launch Mongo on : " $IP ":27654"

mongod --bind_ip=$IP --dbpath=.data --port 27654 --nojournal "$@"
