#!/usr/bin/python2
import sys
import time
import json
import os

with open("./conf.json", 'r') as f:
    config = json.load(f)

AP_NUMBER = config["ap"]["number"]

CURRENT_SESSION = "1"

def sendToDB(data):

    splt = data.split(' ')
    #print(splt)
    if(len(splt) <= 1):
        return
    #print(data)

# 20:29:43.944515 39068888088us tsft 1.0 Mb/s 2417 MHz 11b -49dBm signal -49dBm signal antenna 0 0us #BSSID:ff:ff:ff:ff:ff:ff DA:ff:ff:ff:ff:ff:ff SA:ec:55:f9:0d:cf:86 Probe Request () [1.0 2.0 5.5 11.0 Mbit]

    _time = str(splt[0])
    #print("Time: " + _time)
    strength = str(splt[8]).replace("dBm","")
    #print("Strength: " + strength)
    source = str(splt[17].replace("SA:",""))
    #print("Source: " + source)
    
    quer = "INSERT INTO data (apID,sessionID,sigStrength,strength,sourceMAC,time) VALUES (\'" + AP_NUMBER + "\',\'" + CURRENT_SESSION + "\',\'" + strength + "\',\'" + source+ "\',\'"+_time + "\')"
    os.system("./exec_sql_query.py \"" + quer + "\"")



while True:
    data = sys.stdin.readline()
    if(len(data) > 0):
        sendToDB(data)

