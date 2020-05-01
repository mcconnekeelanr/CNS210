#!/bin/python3

import socket
import threading
from queue import Queue
#target = "www.google.com"
#target = "172.0.0.1"
user = input("what website would you like to scan\n")
target = user

def portscaner(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.2)
    try:
        con = s.connect((target ,port))
        
        print('port',port,'is open')
        con.close()

    except:
        pass

def threader():
    while True:
        ports = q.get()
        portscaner(ports)
        q.task_done()

q = Queue()

for x in range(30):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start() 

for ports in range(1,65535):
    q.put(ports)

    q.join()  
    







