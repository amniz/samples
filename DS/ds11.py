#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose: prime numbers in the range of 0-1000 using 2d array
from DS.util import util
array=[]
for i in range(0,1000,100):
    prime_numbers=util.isPrime(i,i+100)
    array.append(prime_numbers)
counter=0
for i in range(0,1000,100):#getting the difference to the list correctly

    print("prime numbers in the range of",i,"and",i+100,":",end="")
    print(array[counter])
    counter+=1
