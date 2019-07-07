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

from stackreal import Stack
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

pa=checkana(l)
j=sorted(pa)
lo=Stack()
for i in j:
    lo.add(i)
lo.revdisp()
    

