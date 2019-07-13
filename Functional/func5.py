#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N
import sys
try:
	n=int(input("enter the value"))
except ValueError:
	n=int(input("please do enter a integer"))
from Functional.util import harmon
k=harmon(n)
print("sum=",k)
