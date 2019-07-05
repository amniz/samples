#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:This program takes a command-line argument N and prints a table of the powers of 2 that are less than or equal to 2^N. 
# Print the year is a Leap Year or not. 
import sys
n=int(sys.argv[1])
t=2**n

def leapyear(c):
    if c%400==0:
        print("leap year")
    elif c%100==0:
        print ("not leap year")
    elif c%4==0:
        print("leap year")
    else:
        print("not leap year")

if n>31 or n<0:
    print("over flow")
else:
    while (t>0):
        print(t,end="")
        leapyear(t)
        print(end="\n")
        t=int(t/2)
