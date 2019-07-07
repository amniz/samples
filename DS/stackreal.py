
class Node:          #Node classs for storing data of the node
    def __init__(self,data=None,nexp=None):
        self.data=data
        self.nexp=nexp
class Stack:
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
        if self.count==1:
            self.first=None
            return
        last=self.first
        
        c=self.count
        while c>2:
            c-=1
            last=last.nexp
            
        last.nexp=None
    def display(self):
        l=self.first
        if self.count==1:
            return 
        while l.nexp!=None:
            print(l.data)
            l=l.nexp
        print(l.data)
s=Stack()
s.add(10)
s.add(2)
#s.add(3)
s.pop()
s.display()
            
            
