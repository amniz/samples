#@author:Muhammed Nisamudheen
#@version:python 3
#@purpose: check for the anagram and printing it using the reverse order using stack
from DS.util import util


from DS.stackreal import Stack
prime_numbers=util.isPrime(0,1000)  # generating the prime numbers in the range of 0-1000

anagram=util.checkana(prime_numbers)# checking for anagram
sorted_anagram=sorted(anagram)
stack=Stack()  # creating a stack object
for i in sorted_anagram:
    stack.add(i)
stack.revdisp()
