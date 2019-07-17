#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:to give the binary representation of the decimal number typed as the input

from Algorithms.util import util
number=int(input("enter the number"))
result=util.tobinary(number)
print("equallent binary digit of",number,"is ",end="")
print(result)
