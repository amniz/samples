class Node:
    def __init__(self,data=None,nexp=None):
        self.data=data
        self.nexp=nexp
class Queue:
    def __init__(self):
        self.first=Node()
        self.count=0
    def add(self,data):      
        if self.first.data==None:
            self.first.data=data
            self.first.nexp=None
            self.count+=1
        else:
            last=self.first     
            while last.nexp!=None:     
                last=last.nexp
            last.nexp=Node(data,None)
            self.count+=1
    def pop(self):
        first=self.first.nexp
        self.first=first
        self.count-=1
    def display(self):
        l=self.first
        while l.nexp!=None:
            print(l.data)
            l=l.nexp
        print(l.data)
#q=Queue()
#q.add(1)
#q.add(2)
#q.add(30)
#q.pop()
#for i in range(0,100):
#    q.add(i)
#q.display()
        
        
        