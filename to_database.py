#!/usr/bin/python2

import mysql.connector as mariadb
import sys
import time
import json

with open("./conf.json", 'r') as f:
    config = json.load(f)

AP_NUMBER = config["ap"]["number"]

SERVER_IP = config["db"]["ip"]
SERVER_PORT = config["db"]["port"]
SERVER_USER = config["db"]["user"]
SERVER_PASS = config["db"]["pass"]
SERVER_DB = config["db"]["db_name"]

CURRENT_SESSION = "0"
LOCATION = "LOCATION_A"





def connect():
    print("Trying to connect to " + SERVER_IP + ":" +  SERVER_PORT + " as " + SERVER_PASS)
    retry = True
    while retry: 
        try:    
            con = mariadb.connect(host=SERVER_IP,port=SERVER_PORT,user=SERVER_USER, password=SERVER_PASS, database=SERVER_DB)
            retry = False
            print("Connected!\r\n")
        except:
            print("Retrying to connect to " + SERVER_IP + " as " + SERVER_PASS + " in 5 seconds...")
            retry = True
            time.sleep(5)
    return con


connection = connect()

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
    

    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO data (apID,sessionID,sigStrength,strength,sourceMAC,time) VALUES (%s,%s,%s,%s,%s)", (AP_NUMBER, CURRENT_SESSION, strength, source, _time))
    except:
        print("Failed to insert into DB!\r\n")

                
        


while True:
    data = sys.stdin.readline()
    if(len(data) > 0):
        sendToDB(data)

