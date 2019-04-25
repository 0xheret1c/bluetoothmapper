#!/bin/sh
DEVICE=$(printenv 'MONITOR_DEVICE') # Get the device from the enviorment.
chnl=1
while :
do
        sleep $1
        echo "Hopping to channel $chnl"
        iwconfig $DEVICE channel $chnl
        chnl=$(( ( ( $chnl ) % 13) + 1 ))
done

