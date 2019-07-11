#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose: takes a date as input and prints the day of the week that date falls on.

import sys
def daysofWeek():
    m=int(sys.argv[1])#getting the parametrs from command line
    d=int(sys.argv[2])#getting the parametrs from command line
    y=int(sys.argv[3])#getting the parametrs from command line
    y0=int()
    x=int()
    m0=int()
    d0=int()
    y0=y-(14-m)/12#equating and finding out the corresponding day
    x=y0+y0/4-y0/100+y0/400
    m0=m+12*((14-m)/12)-2
    d0=(d+x+31*m0/12)%7
    if (d0==0):#checking for the corresponding day
        return "sunday"
    elif d0==1:
        return "monday"
    elif d0==2:
        return "tuesday"
    elif d0==3:
        return "wednwsday"
    elif d0==4:
        return "thursday"
    elif d0==5:
        return "friday"
    else:
        return "saturday"
    
daysofWeek()

    
