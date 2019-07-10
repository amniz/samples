#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose: prime numbers in range of 0-1000 using queue
from RealQueue import Queue
def isPrime():
        l=[]
        for i in range(10,1000):
           if i==2:
                l.append(i)
           else:
                j=2
                while(j<=i):
                    if i%j==0:
                        break
                       
                    else:
                          j+=1


                if j==i:
                    l.append(i)
        return l
l=isPrime()

def checkana(l):
    ana=set()
    cou=0
    for i in l:
        j=str(i)
        k=sorted(j)
        for j in [x for x in l[cou+1:len(l)]]:
            h=str(j)
            m=sorted(h)
            if k==m:
                ana.add(i)
                ana.add(j)
        cou+=1
    return ana
q=Queue()
anag=checkana(l)
g=sorted(anag)
for i in g:
    #print(i)
    Queue.add(q,i)
Queue.display(q)
