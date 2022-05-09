# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 10:34:42 2021

@author: 20pw33
"""


import socket
s=socket.socket()
host=socket.gethostname()
port=12345
s.connect((host,port))

while True:
      s=input()
      ss=''
      for i in s.split(' '):
          if i =='ESC':
              ss+='ESC ESC'
          elif i=='FLAG':
              ss+='ESC FLAG'
          else:
              ss+=i +' '
      bitstuf=""
      for i in ss.split():
          if i =='ESC':
              bitstuf+='10100011'
          elif i =='FLAG':
              bitstuf='01111110'
          elif ord(i)>=65 and ord(i)<=90:
              ss+=format(int(bin(ord(i))[2:]),'#0008')+' '
              
bitstuf=bitstuf.strip()
print(bitstuf)
for i in bitstuf.split():
    if '11111' in i:
            bitstuf=bitstuf.replace('11111','111110')
print(bitstuf)

s.send(bitstuf.encode())
mess=s.recv(1024).decode()
if mess=='done':
    print("connection")
    break
s.close
         
            
              
    
     
     



































