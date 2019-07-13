#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:implementation of queue using linked list
class Node:#creating node class
    def __init__(self,data=None,nexp=None):
        self.data=data#data attribute
        self.nexp=nexp#next pointer attribute
class Queue:
    def __init__(self):
        self.first=Node()#creating the node 
        self.count=0
    def add(self,data):#adding elements to the node      
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
    def pop(self):#removing first element from the queue
        first=self.first.nexp
        self.first=first
        self.count-=1
    def display(self):#displaying the elements in the queue
        l=self.first
        while l.nexp!=None:
            print(l.data)
            l=l.nexp
        print(l.data)
    def displayforcal(self):#specifically displaying for the calender 
        c=self.count
        print("c",c)
        last=self.first
        ones=0
        while c>0:
            br=0
            while br<7:
                if ones==1 or ones ==2 and  int(last.data)<10:
                    print(last.data,"  ",end="")
                    br+=1
                    c-=1
                    last=last.nexp
                else:
                    br+=1
                    c-=1
                    print(last.data," ",end="")
                    last=last.nexp
            print()
            ones+=1
                
                
#q=Queue()
#q.add(1)
#q.add(2)
#q.add(30)
#q.pop()
#for i in range(0,100):
#    q.add(i)
#q.display()
        
        
        
