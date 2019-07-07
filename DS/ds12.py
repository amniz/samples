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
pa=checkana(l)
listst=set(l)
finaan=[]
d=list(pa)
h=list(listst-pa)
finaan.append(d)
finaan.append(h)
print("the numbers which are prime and anagram in range of 0-1000 are")
print(finaan[0])
print("the numbers which are prime but not anagram in the range of 0-1000 are")
print(finaan[1])
