# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 15:42:15 2021

@author: 20pw33
"""


from datetime import datetime
today=str(datetime.today())
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
import socket
s=socket.socket()

ip=socket.gethostname()
port=12345
s.bind((ip,port))
s.listen(5)
while True:
    c,addr=s.accept()
    c.send(today.encode())
    
    
c.close()