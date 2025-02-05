#!/bin/bash
# monitor.sh

TARGET_IP="192.168.4.1"
LOGFILE="$HOME/downtime.log"

while true; do
    if ! ping -c 1 -W 1 "$TARGET_IP" > /dev/null 2>&1; then
        echo "$(date '+%Y-%m-%d %H:%M:%S') - $TARGET_IP is down" >> "$LOGFILE"
    fi
    sleep 60
done
