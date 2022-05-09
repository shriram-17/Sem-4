# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 20:24:24 2022

@author: shrir
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