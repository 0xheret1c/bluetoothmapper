#!/usr/bin/python3
import os
import sys
import subprocess

#Export env
os.system("./monitormode.py on")
os.system("./dump.py -wifi")
os.system("./monitormode.py off")
