#!/bin/sh

DUMP="../captures/" # Where to store the captured data.
DEVICE=$(printenv 'MONITOR_DEVICE') # Get the device from the enviorment.
DATE=$(date +"%F")

tcpdump -i $DEVICE -vv -n -e -s 256 type mgt subtype probe-req | ../python/to_database.py



