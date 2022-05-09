# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 15:16:49 2021

@author: 20pw33
"""

import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)
          
c,addr = s.accept()
print ('Got connection from', addr)

while True:
        
    response=c.recv(1024).decode()
    ss=''.join(format(ord(i),'b') for i in response)
    c.send(ss.encode())
   
                    
c.close()