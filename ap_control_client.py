#!/usr/bin/python3

import socket
import json
import os

with open("./conf.json", 'r') as f:
    config = json.load(f)


HOST = config["ap_ctrl"]["ip"]      # The server's hostname or IP address
PORT = config["ap_ctrl"]["port"]    # The port used by the server

CURRENT_CHANNEL = 0

STOP = False

def exec(cmd):
    os.system(cmd)

def chhop(hop_to):
    cmd = "./channelhopper.py" + str(hop_to)
    exec(cmd)
    CURRENT_CHANNEL = hop_to

def start_scan():
    cmd = "./start_scan.py"
    exec(cmd)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while not STOP:
        # Get data
        data = repr(s.recv(1024))
        # Split data at ; to get the command, and its arguments
        split = str.split(data,';')
        # Command is the first piece of data
        cmd = split[0]
        # Remove the command, because the rest is the arguments.
        split.remove(split[0])
        args = split
        print("Received: " + data)
        print("Command: " + cmd)
        print("Args:" + args)
        
        if data == "START_SCAN":
            # Start-Scan
            start_scan()
        if data == "STOP_SCAN":
           print("",end='')
        if data == "HOP":
            chhop(args[0])
        if data == "DISCONNECT":
            # Disconnect
            stop = True
            s.close()
