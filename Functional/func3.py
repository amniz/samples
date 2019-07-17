#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose: Determine if it is a Leap Year
# from Functional.util import leapyear
try:
	n=int(input("enter a number which is four digit"))
except ValueError:

	n=int(input("enter an integer"))
if n>999 and n<10000:#ensuring the number is a four digit number
	print(leapyear(n))
else:
	print("not a valid year")
