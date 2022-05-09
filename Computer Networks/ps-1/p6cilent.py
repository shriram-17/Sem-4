# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 11:19:53 2021

@author: 20pw33
"""

import socket
import pickle as p
s=socket.socket()
port=12345
host=socket.gethostname()
s.connect((host,port))

fv=p.loads(s.recv(1024))
print(fv)
s.close()