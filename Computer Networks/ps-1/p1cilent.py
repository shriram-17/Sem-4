# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 11:47:01 2021

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
     if response=='GoodBye':
         break
     
        
s.close()        
     
     



































