from Linkedlist import Linkedlist
from RealQueue import Queue
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
    

class weekDay:    
    def __init__(self):    
        self.a=Queue()
        self.a.add('S')
        self.a.add('  M')
        self.a.add(' T')
        self.a.add(' W')
        self.a.add(' Th')
        self.a.add('F')
        self.a.add('S')
        k=daysofWeek(2,2007)
        j=monthDay(2,2007)
        j1=1
        w=0
        while k>0:
            self.a.add(" ")
            k-=1
            w+=1
        m=1


        while j>0:
            self.a.add(m)
            m+=1
            j-=1
            w+=1
        while w<=55:
            self.a.add(" ")
            w+=1
        print(self.a)

def todis():
    g=weekDay()
    g.a.displayforcal()
todis()

    
