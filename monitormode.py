#!/usr/bin/python3
import os
import json
import sys

with open("./conf.json", 'r') as f:
    config = json.load(f)

DEV = config["ap"]["network_monitor_dev"]

#Turn monitor-mode for DEVICE on.
def on():
	os.system("ifconfig " + DEV + " down")
	os.system("iwconfig " + DEV + " mode monitor")
	os.system("ifconfig " + DEV + " up")


#Turn monitor-mode for DEVICE off.
def off():
	os.system("ifconfig " + DEV + " down")
	os.system("iwconfig " + DEV + " mode managed")
	os.system("ifconfig " + DEV + " up")


if (sys.argv[1] == "on"):
	on()
elif (sys.argv[1] == "off"):
	off()


