# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 15:07:04 2021

@author: 20pw33
"""

import socket
s=socket.socket()
host=socket.gethostname()
port=12345
s.connect((host,port))

while True:
     msg=input('Enter the message to be sent:')
     s.send(msg.encode())
     response=s.recv(1024).decode()
     print(f'Message from the server :{response}')
      
     a=input('Do you want to continue:')
     if a=='N':
          break
  
s.close()        
     