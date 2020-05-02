#!/bin/python3

import signal
import socket
import threading
from queue import Queue
#target = "www.google.com"
#target = "172.0.0.1"
user = input("what website would you like to scan\n")
target = user
num1 = input("pick a port number")
num2 = input("pick a port number")
port1 = int(num1)
port2 = int(num2) +1





def portscaner(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.2)
    try:
        con = s.connect((target ,port))
        
        print('port',port,'is open')
        con.close()
   
    except KeyboardInterrupt:
        print("cancelled thanks for choosing keelans port scanner")

    except:
        pass
    
    
        

def threader():
    while True:
        ports = q.get()
        portscaner(ports)
        q.task_done()
q = Queue()

for x in range(1):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start() 
    
        
for ports in range(port1,port2):
    q.put(ports)

    q.join()  
    

print("no more")





