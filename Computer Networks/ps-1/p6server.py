# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 11:08:00 2021

@author: 20pw33
"""


   

import socket
import pickle as p
s=socket.socket()
host=socket.gethostname()
port=12345
d={1:'2',2:'3',3:'4'}
s.bind((host,port))
s.listen(3)

c,a=s.accept()
obj=p.dumps(d)
c.send(obj)
   
c.close()