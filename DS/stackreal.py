#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:implementation of stack using linked list
class Node:          #Node classs for storing data of the node
    def __init__(self,data=None,nexp=None):
        self.data=data#making the data attribute
        self.nexp=nexp#attribute which points towards the next data element
class Stack:
    def __init__(self):
        self.first=Node()#creating a node element
        self.count=0
    def add(self,data):#adding the element to the end of the stack
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
    def pop(self):#poping out from the stack
        if self.count==1:
            self.first=None
            self.count-=1
            return 
        last=self.first
        
        c=self.count
        while c>2:
            c-=1
            last=last.nexp
            
        last.nexp=None
        self.count-=1
##    def pop(self):
##        if self.count==1:
##            dat=self.first.data
##            self.first=None
##            self.count-=1
##            return dat
##        last=self.first
##        
##        c=self.count
##        while c>2:
##            c-=1
##            last=last.nexp
##            
##        last.nexp=None
##        self.count-=10
    def display(self):#display method to display the elements in the stack
        l=self.first
        if self.count==1:
            return 
        while l.nexp!=None:
            print(l.data)
            l=l.nexp
        print(l.data)
    def revdisp(self):#reverse display method to display the elements reverse in the stack
        
        c=self.count
        while c>0:
            last=self.first
            n=1
            m=0
            while n<c:
                last=last.nexp
                n+=1
                m+=1
            print(last.data)
            c-=1
        
#s=Stack()
#s.add(10)
#s.add(2)
#s.add(3)
#s.pop()
#s.display()
            
            
