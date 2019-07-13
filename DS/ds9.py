#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose: prints the calender using queue
from Linkedlist import Linkedlist
from RealQueue import Queue
from util import util


class weekDay:
    def __init__(self):
        self.a=Queue()#initializing the queue variable
        self.a.add('S')#adding the elements in the queue
        self.a.add('  M')
        self.a.add(' T')
        self.a.add(' W')
        self.a.add(' Th')
        self.a.add('F')
        self.a.add('S')
        k=util.daysofWeek(2,2007)
        j=util.monthDay(2,2007)
        j1=1
        w=0
        while k>0:#adding the empty element in the queue
            self.a.add(" ")
            k-=1
            w+=1
        m=1


        while j>0:#adding the date to the queue
            self.a.add(m)
            m+=1
            j-=1
            w+=1
        while w<=55:#adding the rest of the empty 
            self.a.add(" ")
            w+=1
        print(self.a)

def todis():
    g=weekDay()
    g.a.displayforcal()
todis()
