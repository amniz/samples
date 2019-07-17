#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose: prime numbers in range of 0-1000 using queue
from DS.RealQueue import Queue
from DS.util import util

l=util.isPrime(0,1000)


q=Queue()#creating an empty queue
anag=util.checkana(l)#checking for anagram
g=sorted(anag)#sorting the elements
for i in g:
    #print(i)
    Queue.add(q,i)#adding the elements to the queue
Queue.display(q)
