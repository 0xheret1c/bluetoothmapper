#!/bin/sh

DUMP="../captures/" # Where to store the captured data.
DEVICE=$(printenv 'MONITOR_DEVICE') # Get the device from the enviorment.
DATE=$(date +"%F")

tcpdump -i $DEVICE -w $DUMP"wireless_$DATE.cap" -n -v -e -s 256 type mgt subtype probe-req


