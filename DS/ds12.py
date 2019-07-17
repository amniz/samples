#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose: prime numbers in specific range using 2d array.
from DS.util import util
prime_numbers=util.isPrime(0,1000)#getting the prime numbers


anagram_num=util.checkana(prime_numbers)#checking whether they are anagram or not
listst=set(prime_numbers)
final_list=[]
anagram_list=list(anagram_num)
differentiated_list=list(listst-anagram_num)#differentiating the element
final_list.append(anagram_list)
final_list.append(differentiated_list)
print("the numbers which are prime and anagram in range of 0-1000 are")
print(final_list[0])
print("the numbers which are prime but not anagram in the range of 0-1000 are")
print(final_list[1])
