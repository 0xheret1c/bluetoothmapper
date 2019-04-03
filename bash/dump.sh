#!/bin/sh

DUMP="../captures/" # Where to store the captured data.
DEVICE=$(printenv 'MONITOR_DEVICE') # Get the device from the enviorment.
DATE=$(date +"%F")

./channelhopper.sh 5 &
tcpdump -i $DEVICE -w $DUMP"wireless_$DATE.cap" -n -e -s 256 type mgt subtype probe-req


