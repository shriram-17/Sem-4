

import socket

s=socket.socket()

port=12345

host=socket.gethostname()

s.bind((host,port))
s.listen(5)
c,addr=s.accept()
print(f'Got Connection from {addr}')
while True:
    string = c.recv(1024).decode()

    str=string.split()[2:]
    print(str)
    string=string.split()
    print(string)
    wrt=''
    for x in str:
        wrt+=x+' '
    if string[1]=='Add':
        print('Added The Event')
        fp = open('file.txt', 'w')
        fp.write(wrt)
        fp.close()
    if string[1]=='Remove':
        print('Remove the Event')
        wt=''
        for x in string:
            wt += x
        f = open('file.txt', 'r')
        a = wt.split()[2:]
        lst = []
        for line in f:
            for word in a:
                if word in line:
                    line = line.replace(a, '')
            lst.append(line)
        f.close()
        fp = open('file.txt', 'w')
        for line in lst:
            f.write(line)
        fp.close()
    if string[1]=='Update':
        print('Update the Event')
        fp= open("file.txt",'r')
        data = fp.read()
        data=data.split()
        data.remove(data[1])
        data.append(string[3])
        fp.close()
        data=' '.join(data)
        fp = open("file.txt", 'w')
        fp.write(data)
        fp.close()
    if string[1]=='Get':
        print('Get The Data')
        fp=open('file.txt','r')
        for line in fp.readlines():
            if wrt in line:
             continue
        print(line)

s.close()
