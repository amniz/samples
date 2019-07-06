from Node import Dnode
class Deque:
    def __init__(self):
        self.dq=Dnode()
        self.count=0
    def addFront(self,data):
        if self.count==0:
            print("adding initial data",data)
            self.dq.data=data
            self.count+=1
        first=self.dq
        while first.prev!=None:
            first=first.prev
        print("adding data",data)
        first.prev=Dnode(data,first,None)
        self.count+=1
    def addRear(self,data):
        if self.count==0:
            self.dq.data=data
            self.count+=1
        first=self.dq
        while first.nexp!=None:
            first=first.nexp
        first.nexp=Dnode(data,None,first)
        self.count+=1
    def removeFront(self):
        if self.count==0:
            return
        else:
            first=self.dq
            c=1
            while first.prev!=None:
                first=first.prev
                c+=1
            temp=self.dq
            while c>2:
                temp=temp.prev
                c-=1
            temp.prev=None
            self.count-=1
    def removeRear(self):
        if self.count==0:
            return
        else:
            last=self.dq
            k=1
            while last.nexp!=None:
                last=last.nexp
                k+=1
            temp=self.dq
            while k>2:
                temp=temp.nexp
            temp.nexp=None
            self.count-=1
    def isEmpty(self):
        if self.count==0:
            return True
        else:
            return False
    def size(self):
        return self.count
    def display(self):
        last=self.dq
        while last.prev!=None:
            last=last.prev
        while last.nexp!=None:
            print(last.data)
            last=last.nexp
        print(last.data)
        
def main():
        q=Deque()
        l=Deque()
        s=input("enter the string")
        for i in s:
            q.addFront(i)
            l.addRear(i)
        q.display()
        l.display()
        le=q.size()
        while le>0:
            if q.dq.data==l.dq.data:
                l.removeRear()
                q.removeFront()
                q=q.nexp
                l=l.prev
                
            else:
                break
        if isEmpty==True:
            print("palindrome")
        else:
            print("Not a Palindrome")
if __name__=='__main__':
        main()
            
        
        
                
                
