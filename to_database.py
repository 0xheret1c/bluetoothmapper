#!/usr/bin/python2
import sys
import time
import json
import os

with open("./conf.json", 'r') as f:
    config = json.load(f)

AP_NUMBER = config["ap"]["number"]

CURRENT_SESSION = "0"
LOCATION = "LOCATION_A"




def sendToDB(data):
    splt = data.split()
    if(len(splt) <= 0):
        return
    
    _time = splt[0]
    strength = splt[6]
    source = splt[13].replace("SA:","")
    print("Time: " + _time)
    print("Strength: " + strength)
    print("Source: " + source)
    
    query = "INSERT INTO data (apID,sessionID,sigStrength,strength,sourceMAC,time) VALUES (" + AP_NUMBER + "," +CURRENT_SESSION + "," + strength + "," + source,_time + ")"
    os.system("./exec_sql_query.py \"" + query + "\"")



                
        


while True:
    data = sys.stdin.readline()
    if(len(data) > 0):
        sendToDB(data)

