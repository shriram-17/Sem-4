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
          

while True:
        c,addr = s.accept()
        print ('Got connection from', addr)
        
        while True:
    
            bitstuf=c.recv(1024).decode()
            print(bitstuf)
        
        for i in bitstuf.split():
            if '111110' in i:
                bitstuf=bitstuf.replace('111110','11111')
        unstuffing=''
        for i in bitstuf.split():
            if i=='10100011':
                unstuffing+='ESC'
            elif i=='01111110':
                unstuffing+='FLAG'
            else:
                unstuffing+=chr(int(i,2))+' '

        unstuffing=unstuffing.replace('ESC FLAG', 'FLAG')
        unstuffing=unstuffing.replace('ESC ESC', 'ESC')
        unstuffing=unstuffing.strip(' ')
        print(unstuffing)
        k="done"
        s.send(k.encode)
        break
c.close()
        
        
        