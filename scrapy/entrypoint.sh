#!/usr/bin/env bash
set -e

# Build list of available proxies periodically
#while true; do
#  create_proxy_list.py --output=/tmp/proxy_list.txt --logfile=/var/log/proxy_list.log
#  sleep 6h
#done &

#apt-get update
#apt-get install -y gcc
#pip install -r ./requirements.txt

exec "$@"
