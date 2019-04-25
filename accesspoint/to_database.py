#!/usr/bin/python2

import mysql.connector as mariadb
import sys
import time
LOCATION = "LOCATION_A"
AP_NUMBER = "0"
SERVER_IP = "127.0.0.1"
SERVER_DB = "db_raw_data"
SERVER_PORT = "3306"
SERVER_USER = "root"
SERVER_PASS = "root"



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
        cursor.execute("INSERT INTO captures (location,ap,time,strength,source) VALUES (%s,%s)", (LOCATION, AP_NUMBER,_time,strength,source))
    except:
        print("Failed to insert into DB!")
    print(" ")
                
        


while True:
    data = sys.stdin.readline()
    if(len(data) > 0):
        sendToDB(data)

