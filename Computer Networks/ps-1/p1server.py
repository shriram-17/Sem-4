# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 10:44:38 2021

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
    if response=='Bye':
        c.send(b'GoodBye')
        break
    else:
        c.send(b'Ok')
    


c.close()