#!/usr/bin/python3

import socket
import json

with open("./conf.json", 'r') as f:
    config = json.load(f)

HOST = config["ap_ctrl"]["ip"]      # The server's hostname or IP address
PORT = config["ap_ctrl"]["port"] # The port used by the server

STOP = False

def get_command():
    invalidCommand = True
    while invalidCommand:
        cmd = input(">>> ")
        if cmd == "start_scan":
            return "START_SCAN"
        if cmd == "stop_scan":
            return "STOP_SCAN"
        print("Unknown command \"" + cmd +"\"")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    
    with conn:
        print("New connection from " + addr)    
        while not STOP:
            payload = get_command()

            conn.sendall(str.encode(payload))
            print("Sent: " + payload)