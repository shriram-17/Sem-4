# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 13:56:12 2022

@author: MAB46
"""

import socket

s=socket.socket()

port=12345

host=socket.gethostname()

s.connect((host,port))





value=int(input("Enter the Numbers /n 1.Add a new calendar event /n 2.Remove a calendar /n 3.upadate a calendar /n 4. get the Event"))

if value==1:
    string=(input('Enter the Values for adding the event'))
  
    s.send(string.encode())
elif value==2:
    string=(input('Enter the Values for removing the event'))
    s.send(string.encode())
    
elif value==3:
    string=(input('Enter the Values for update the event'))
    s.send(string.encode())
elif value==4:
    string=(input('Enter the Values for Get the event'))
    s.send(string.encode())
    
s.close()         