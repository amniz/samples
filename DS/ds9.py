#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose: prints the calender using queue
from DS.Linkedlist import Linkedlist
from DS.RealQueue import Queue
from DS.util import util


class weekDay:
    def __init__(self):
        self.calender=Queue()#initializing the queue variable
        self.calender.add('S')#adding the elements in the queue
        self.calender.add('  M')
        self.calender.add(' T')
        self.calender.add(' W')
        self.calender.add(' Th')
        self.calender.add('F')
        self.calender.add('S')
        start_of_month=util.daysofWeek(2,2007)

        days_in_month=util.monthDay(2,2007)
        # j1=1
        counter_for_adding_dates=0
        while start_of_month>0:#adding the empty element in the queue
            self.calender.add(" ")
            start_of_month-=1
            counter_for_adding_dates+=1
        add_days_of_month=1


        while days_in_month>0:#adding the date to the queue
            self.calender.add(add_days_of_month)
            add_days_of_month+=1
            days_in_month-=1
            counter_for_adding_dates+=1
        while counter_for_adding_dates<=55:#adding the rest of the empty
            self.calender.add(" ")
            counter_for_adding_dates+=1
        print(self.calender)

def display():
    weekdayobject=weekDay()
    weekdayobject.calender.displayforcal()
display()
