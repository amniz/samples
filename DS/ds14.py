#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose: prime numbers in range of 0-1000 using queue
from DS.RealQueue import Queue
from DS.util import util

prime_number=util.isPrime(0,1000)


q=Queue()#creating an empty queue
anagrams=util.checkana(prime_number)#checking for anagram
sorted_anagram=sorted(anagrams)#sorting the elements
for i in sorted_anagram:
    #print(i)
    Queue.add(q,i)#adding the elements to the queue
Queue.display(q)
