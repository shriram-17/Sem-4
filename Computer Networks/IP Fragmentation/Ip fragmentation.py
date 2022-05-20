import math

data =int(input("Enter The Packet Size:"))
Mtu=int(input("Enter The Mtu Size:"))
header=20
Mtu=Mtu-header
data=data-header
iterations=data/Mtu
print(iterations)
iterations=math.ceil(iterations)
print(iterations)
offset=[]
lst=[]
for i in range(1,iterations+1):
    if i==iterations:
        x=data-Mtu*(iterations-1)
        lst.append(x)
    else:
        lst.append(Mtu)
print(lst)
for i in range(0,len(lst)):
    if i==0:
       var=0
       offset.append(var)
    var=lst[i]/8
    offset.append(var)
print(offset)

sum1=[]
for i in range(0,len(offset)):
    if i==0:
       var=0
       sum1.append(var)
    else:
        var=sum(offset[:i+1])
        sum1.append(var)
print(sum1)
mf=[]
for i in range(0,len(lst)):
    if i==len(lst)-1:
        var=0
        mf.append(var)
    else:
        var=1
        mf.append(var)
print(mf)
names=['first','second','third','fourth','fifth','sixth','seventh','eigth']
n=len(lst)
print(f"There can be {names[n-1]} fragments send:")
for (a,f,b,c) in zip(names,lst, sum1, mf):
    print (f"The {a} fragment data size is {f} , offset = {b} ,MF flag = {c}")
