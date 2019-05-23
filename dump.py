
#!/usr/bin/python3
import os
import json

with open("./conf.json", 'r') as f:
    config = json.load(f)

DEV = config["ap"]["network_monitor_dev"]

os.system("tcpdump -i " + DEV + " -vv -n -e -s 256 type mgt subtype probe-req | ../to_database.py")


