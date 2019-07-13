#@author:Muhammed Nisamudheen
#@version:python 3
#@purpose: check for the anagram and printing it using the reverse order using stack
from DS.util import util
l=util.isPrime()

from DS.stackreal import Stack


pa=util.checkana(l)#checking for anagram
j=sorted(pa)
lo=Stack()
for i in j:
    lo.add(i)
lo.revdisp()
