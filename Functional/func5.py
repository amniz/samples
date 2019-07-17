#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N
import sys
from Functional.util import harmonic_number
try:  # checking whether the given data is correct or not
	value=int(input("enter the N'th harmonic number"))
except ValueError as e:
	print("enter an integer",e)

result=harmonic_number(value)
print("sum=",result)
