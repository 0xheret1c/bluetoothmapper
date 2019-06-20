#!/usr/bin/python2

import mysql.connector as mariadb
import sys
import time
import json

with open("./conf.json", 'r') as f:
    config = json.load(f)


SERVER_IP   = config["db"]["ip"]
SERVER_PORT = config["db"]["port"]
SERVER_USER = config["db"]["user"]
SERVER_PASS = config["db"]["pass"]
SERVER_DB   = config["db"]["db_name"]


def connect():
    print("Trying to connect to " + SERVER_IP + ":" +  SERVER_PORT + " as " + SERVER_PASS)
    retry = True
    while retry: 
        try:    
            con = mariadb.connect(host=SERVER_IP,port=SERVER_PORT,user=SERVER_USER, password=SERVER_PASS, database=SERVER_DB)
            retry = False
            #print("Connected!\r\n")
        except:
            print("Retrying to connect to " + SERVER_IP + " as " + SERVER_PASS + " in 5 seconds...")
            retry = True
            time.sleep(5)
    return con


def exec_query(query):
    
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute(str(query))
        print("Executed: " + str(query))
    except:
        print("Failed to insert into DB!\n Query: "+query+"\r\n")


if(len(sys.argv)== 2):
    exec_query(sys.argv[1])
