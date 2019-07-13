#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose: prime numbers in specific range using 2d array.
from DS.util import util
l=util.isPrime()#getting the prime numbers


pa=util.checkana(l)#checking whether they are anagram or not
listst=set(l)
finaan=[]
d=list(pa)
h=list(listst-pa)#differentiating the element
finaan.append(d)
finaan.append(h)
print("the numbers which are prime and anagram in range of 0-1000 are")
print(finaan[0])
print("the numbers which are prime but not anagram in the range of 0-1000 are")
print(finaan[1])
