#!/usr/bin/python3
import json
import os
import subprocess

def command(usr,pw,ip,cmd):
    sub=subprocess.Popen(["/usr/bin/sshpass", "-p",pw,"ssh","-o","stricthostkeychecking=no",usr +"@"+ ip,"export DISPLAY=:0 && echo \"" +pw+"\" | sudo -E -S -k "+cmd],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)

with open("./ap_control_conf.json", 'r') as f:
    config = json.load(f)

AP1_USER = config["ap1"]["usr"]
AP1_PASS = config["ap1"]["pass"]
AP1_IP   = config["ap1"]["ip"]      

AP2_USER = config["ap2"]["usr"]
AP2_PASS = config["ap2"]["pass"]
AP2_IP   = config["ap2"]["ip"]      

AP3_USER = config["ap3"]["usr"]
AP3_PASS = config["ap3"]["pass"]
AP3_IP   = config["ap3"]["ip"]      

command(AP1_USER,AP1_PASS,AP1_IP,"/home/" + AP1_USER + "/bluetoothmapper/start_scan.py")      
command(AP2_USER,AP2_PASS,AP2_IP,"/home/" + AP2_USER + "/bluetoothmapper/start_scan.py")      
command(AP3_USER,AP3_PASS,AP3_IP,"/home/" + AP3_USER + "/bluetoothmapper/start_scan.py")