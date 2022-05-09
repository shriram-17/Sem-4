data=input()
l=len(data)
r=0
while l+r+1>2**r:
    r=r+1
j = 0
k = 1
res=''
for i in range(1,l+r+1):
        if(i == 2**j):
            res = res + '0'
            j += 1
        else:
            res=res+data[-1*k]
            k += 1

codeword=res[::-1]
print(res)

rbits=list()
for i in range(0,r):
    rbits.append(2**i)

res=[int(x) for x in list(res)]

paritybits=[]
print(res)
for p in rbits:
    j=p-1
    tot=0
    while j<len(res):
        tot=tot+sum(res[j:j+p])
        j+=p+p    
    paritybits.append(tot%2)    
i=0
for b in rbits: 
    res[b-1]=paritybits[i]
    i+=1

res=[str(x) for x in res]
res=res[::-1]
codeword=''.join(res)
print(codeword)


    
    
