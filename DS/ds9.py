from Linkedlist import Linkedlist
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
    
class WeekDay:
    def __init__(self):
        self.week=Linkedlist()
    def pop(self,index):#poping at the specified position
        last=self.week
        if index==1:#poping at the first position
            self.week=self.week.first.nexp
            self.week.count-=1
            return self.week.frist.data
        elif index>1 and index<self.week.count:#poping at the position between first and last
            co=2
            c=2
            temp=self.week.first
            while c<=index:

                temp=temp.nexp
                c += 1

            while co<index:
                

                last=last.nexp
                co += 1
            
            last.nexp=temp.nexp
            #self.week.count-=1
            return temp.data
        else:#poping at the position of last
            i=2
            last=self.week.first
            while i<self.week.count:
                last=last.nexp
                i+=1
            dat=last.data
            last.nexp=None
            #self.week.count-=1
            return dat
        
    
    
a=WeekDay()
a.week.add('S')
a.week.add('M')
a.week.add('T')
a.week.add('W')
a.week.add('Th')
a.week.add('F')
a.week.add('S')
k=daysofWeek(2,2007)
j=monthDay(2,2007)
j1=1
while k>0:
    a.week.add(" ")
    k-=1

while j>0:
    a.week.add(j1)
    j1+=1
    j-=1
while j<23:
    print(a.pop(j))
    j+=1
    
