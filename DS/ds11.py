#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose: prime numbers in the range of 0-1000 using 2d array
from util import util
r=[]
for i in range(0,1000,100):
    k=util.isPrime(i,i+100)
    r.append(k)
h=0
for i in range(0,1000,100):#getting the difference to the list correctly

    print("prime numbers in the range of",i,"and",i+100,":",end="")
    print(r[h])
    h+=1
