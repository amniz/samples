#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N 
import sys
try:
	n=int(input("enter the value"))
except ValueError:
	n=int(input("please do enter a integer"))

t=1
sum=0
while(t<=n):#generating and printing the harmonic number
    sum=1/t
    t+=1
    print("1/",t,"=",1/t)
print(sum)
