#!/usr/bin/python2
import sys      # sys.stdin.readline() to read from standard input.
import json     # loading the json conf
import os       # os.system to execute ./to_database.py

with open("./conf.json", 'r') as f:
    config = json.load(f)

AP_NUMBER = config["ap"]["number"]

CURRENT_SESSION = "1" #Currently hardcoded due to time constraints.

# Pretty much does what the name suggests.
# Builds a quere out of the given input, which should be the tcpdump output as seen below.
# 
def sendToDB(data):

    splt = data.split(' ')
    
    # Filter out some trash input.
    if(len(splt) <= 1):
        return


    # Sample output of tcpdump:
    # 20:29:43.944515 39068888088us tsft 1.0 Mb/s 2417 MHz 11b -49dBm signal -49dBm signal antenna 0 0us BSSID:ff:ff:ff:ff:ff:ff DA:ff:ff:ff:ff:ff:ff SA:ec:55:f9:0d:cf:86 Probe Request () [1.0 2.0 5.5 11.0 Mbit]
    # Currently pretty messy to split up the output of tcpdump. 
    # Better option would be to parse the libcap format with its library.
    
    _time = str(splt[0])                       # First part of the string is the time 
    strength = str(splt[8]).replace("dBm","")  # 8th part is the signal-strength. Remove dBm so we get a clean integer.
    source = str(splt[17].replace("SA:",""))   # 17th. part is the source address. Remove SA: so only the address stays.

    # Add single quotation marks here for better readabillity
    _apnum      = "\'" + AP_NUMBER       + "\'"
    _cursession = "\'" + CURRENT_SESSION + "\'"
    _strength   = "\'" + strength        + "\'"
    _source     = "\'" + source          + "\'"
    __time      = "\'" + _time           + "\'"

    # Built the query . 
    quer = "INSERT INTO data (apID,sessionID,sigStrength,strength,sourceMAC,time) VALUES (" + _apnum + "," + _cursession + "," + _strength + "," + _source+ ","+__time + "\');"
    
    # Execute the query; Add quotation marks so the arg gets transfered as one string, and not as multiple args.
    os.system("./exec_sql_query.py \"" + quer + "\"")


# Keep reading from standard input forever.
# Should add some mechanism to stop the whole process
while True:
    data = sys.stdin.readline()
    
    # Sometimes we get empty input
    # which might crash the function.
    if(len(data) > 0):
        sendToDB(data)

