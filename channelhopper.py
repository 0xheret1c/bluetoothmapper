#!/usr/bin/python3
import sys
import os
import json

with open("./conf.json", 'r') as f:
    config = json.load(f)

DEV = config["ap"]["network_monitor_dev"]
channel = sys.argv[0]

print("Hopping to channel " + channel + ".")
os.system("iwconfig " + DEV + "channel " + channel)


