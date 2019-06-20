#!/usr/bin/python3
import os
import json
import sys

# Load config to get device settings.
with open("./conf.json", 'r') as f:
    config = json.load(f)

WIFI_DEV = config["ap"]["network_monitor_dev"]
BT_DEV = config["ap"]["bluetooth_dev"]


def sniffWifi():
        command = "tcpdump -i " + WIFI_DEV + " -vv -n -e -s 256 type mgt subtype probe-req | ./to_database.py"
        os.system(command)

def sniffBluetooth():
        command = "tcpdump -vv -i " + BT_DEV  #| ../to_database.py"
        os.system(command)

sniffWifi()
#os.system("./printlogo.py")

# Dump depending on arg. Default is bluetooth
# if(argc > 1):
#     print("Too many arguments!")
#     exit()
# elif(argc == 1):
#     if(argv[0] == "w" or argv[0] == "wifi"):
#         sniffWifi()
#     else:
#         sniffBluetooth()



