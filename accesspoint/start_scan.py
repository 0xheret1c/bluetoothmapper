#!/usr/bin/python3
import os
import sys
import subprocess

#Export env
os.system("../bash/monitormode.sh on")
sub = subprocess.Popen(["../bash/channelhopper.sh","5"])
os.system("../bash/dump.sh")
os.system("../bash/monitormode.sh off")
