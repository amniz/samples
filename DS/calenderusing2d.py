#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose: prints the claender of a given date using a 2d array.
def daysofWeek(mon,yea):
    m=mon
    d=1
    y=yea
    y0=int()
    x=int()
    m0=int()
    d0=int()
    y0=y-(14-m)/12
    x=y0+y0/4-y0/100+y0/400
    m0=m+12*((14-m)/12)-2
    d0=(d+x+31*m0/12)%7
    return d0
def Leap(n):
    if n%400==0:
        return True
    elif n%100==0:
        return False
    elif n%4==0:
        return True
    else:
        return False
def monthDay(m,y):
    i=m
    if i==2:
        if Leap(y):
            return 30
        else:
            return 29
    elif i in [4,6,9,11]:
        return 31
    else:
        return 32 
    

import sys
m=int(sys.argv[1])
y=int(sys.argv[2])
k=daysofWeek(m,y)
d=int(k)
go=d+9
days=[x for x in range(1,monthDay(m,y))]
print("     python cal",m," ",y)
print("    S   M  T   W  Th   F   S")
li=[]
val=42
c=0
while val>0:
    g=[]
    n=0
    
    while n<=6:
        while d>0:
            g.append(" ")
            n+=1
            val-=1
            d-=1
        try:
            g.append(days[c])
            c+=1
            n+=1
            val-=1
        except:
            g.append(" ")
            c+=1
            n+=1
            val-=1
    li.append(g)

for k in li:
    
    n=0
    while n<=6:
        if go>0:
            print("  ",k[n],end="")
            n+=1
            go-=1
        else:
            print(" ",k[n],end="")
            n+=1
    print()
        
        
    



