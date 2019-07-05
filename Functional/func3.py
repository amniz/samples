#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose: Determine if it is a Leap Year
n=int(input("enter a number which is four digit"))
if n>999 and n<10000:
    if n%400==0:
        print ("its a leap year")
    elif n%100==0:
        print("its not a leap year")
    elif n%4==0:
        print("its a leap year")
    else:
        print("not a leap year")
else:
    print("please enter a valid year")
