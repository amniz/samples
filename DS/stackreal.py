from Linkedlist import Linkedlist
class Stack:
    def __init__(self):
        self.ele=Linkedlist()
    def add(self,data):
        self.ele.add(data)
    def pop(self):
        self.ele.pop()
    def disp(self):
        l=self.ele.first
        tem=self.ele.first
        h=self.ele.size()
        while h>0:
            c=0
            while l.nexp!=None:
                l=l.nexp
                c+=1
            print("disp",l.data)
            
            while c>1:
                tem=tem.nexp
            tem.nexp=None
            h-=1
a=Stack()
a.add(10)
a.add(2)
a.add(5)
a.disp()
