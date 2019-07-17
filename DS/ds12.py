#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose: prime numbers in specific range using 2d array.
from DS.util import util
l=util.isPrime(0,1000)#getting the prime numbers


pa=util.checkana(l)#checking whether they are anagram or not
listst=set(l)
final=[]
d=list(pa)
h=list(listst-pa)#differentiating the element
final.append(d)
final.append(h)
print("the numbers which are prime and anagram in range of 0-1000 are")
print(final[0])
print("the numbers which are prime but not anagram in the range of 0-1000 are")
print(final[1])
