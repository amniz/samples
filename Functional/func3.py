#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose: Determine if it is a Leap Year
try:
	n=int(input("enter a number which is four digit"))
except ValueError:
	n=int(input("enter an integer"))
if n>999 and n<10000:#ensuring the number is a four digit number
    if n%400==0:#checking whether divisble by 400
        print ("its a leap year")
    elif n%100==0:#checking whether divisble by 100
        print("its not a leap year")
    elif n%4==0:#checking whether divisble by 4
        print("its a leap year")
    else:
        print("not a leap year")
else:
    print("please enter a valid year")
