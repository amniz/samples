class Node:
    def __init__(self,data=None,nexp=None):
        self.data=data
        self.nexp=nexp
class Queue:
    def __init__(self):
        self.q=Node()
        self.count=0
        
    def enqueue(self,data):
        last=self.q
        if self.count==0:
            
            last.data=data
            last.nexp=None
            self.count+=1
            
        else:
            while last.nexp!=None:
                last=last.nexp
            last.nexp=Node(data)
            self.count+=1
    def deque(self):
        dat=self.q.data
        self.q=self.q.nexp
        self.count-=1
        return dat
    def isempty(self):
        if self.count==0:
            return True
        else:
            return False
    def size(self):
        return self.count
    def display(self):    #display method to print all the elements in the linked list
        if self.count==0:
            return "no elements"
        last=self.q
        while last.nexp!=None:

           print("element is",last.data,"nexp",last.nexp,"id is ",id(last.data))

           last=last.nexp
        print(last.data)
    
    
            
                
a=Queue()
a.enqueue(10)
a.enqueue(2)
a.display()
k=a.deque()
print(k)
a.deque()
print(a.display())
print(a.size())
print(a.isempty())


