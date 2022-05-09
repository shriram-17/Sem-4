# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 15:42:16 2021

@author: 20pw33
"""
import socket
s=socket.socket()
ip=socket.gethostname()
port=12345
s.connect((ip,port))
while True:
    response=s.recv(1024).decode()
    response1 =s.recv(1024).decode()
    print("The Current date is  ",response)
    print("The curRent time is",response1)
s.close()
