#!/usr/bin/python3
import os	# Executing ifconfig and iwconfig
import json # Reading the conf
import sys	# Reading args

# Load the config to get the desired monitor-device.
with open("./conf.json", 'r') as f:
    config = json.load(f)

# Monitor device name.
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
else:
	print("Not enough arguments!")


