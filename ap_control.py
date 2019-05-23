#!/usr/bin/python3
import selectors
import socket
import json
import os
import types

with open("./ap_control_conf.json", 'r') as f:
    config = json.load(f)

HOST = config["ap_ctrl"]["ip"]      # The server's hostname or IP address
PORT = config["ap_ctrl"]["port"]    # The port used by the server

STOP = False

def create_session():
    query = "INSER INTO ..."
    os.system("./exec_db_query.py \"" + query + "\"")

def get_command():
    invalidCommand = True
    while invalidCommand:
        cmd = input(">>> ")
        if cmd == "start_scan":
            return "START_SCAN"
        if cmd == "stop_scan":
            return "STOP_SCAN"
        print("Unknown command \"" + cmd +"\"")

sel = selectors.DefaultSelector()


def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print("accepted connection from", addr)
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)


def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            data.outb += recv_data
        else:
            print("closing connection to", data.addr)
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print("echoing", repr(data.outb), "to", data.addr)
            sent = sock.send(data.outb)  # Should be ready to write
            data.outb = data.outb[sent:]

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((HOST, PORT))
lsock.listen()
print("listening on " + HOST + ":" + str(PORT))
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)

try:
    while True:
        events = sel.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                accept_wrapper(key.fileobj)
            else:
                service_connection(key, mask)
except KeyboardInterrupt:
    print("caught keyboard interrupt, exiting")
finally:
    sel.close()
    
    
    