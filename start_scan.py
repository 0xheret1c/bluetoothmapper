#!/usr/bin/python3
import os


os.system("./monitormode.py on")
os.system("./dump.py -wifi")
os.system("./monitormode.py off")
