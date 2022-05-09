# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 14:59:28 2021

@author: 20pw33
"""

import socket
s=socket.socket()
host=socket.gethostname()
port=12345
s.connect((host,port))

while True:
     msg=input('Enter the message:')
     s.send(msg.encode())
     response=s.recv(1024).decode()
     print(response)
     break   
s.close()        
     