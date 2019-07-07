class Node:
    def __init__(self,data=None,nexp=None):
        self.data=data
        self.nexp=nexp
class Queue:
    bal=10000000
    def __init__(self):
        self.q=Node()
        self.count=0
        
    def enqueue(self,data=None):
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
    def check(self):
        print("in check")
       
        fw=int(input("1->deposit\n2->withdrawl"))
        if fw==1:
            damnt=int(input("enter the amount to be deposited"))
            cls.bal+=damnt
            a.data+=data
            ch=bool(input("do you wish to continue for an another transaction"))
            if ch==True:
                check()
            else:
                
                return
        elif fw==2:
            wamnt=int(input("enter the amount to be withdrawn"))
            if wmnt<bal-5000 and self.data>=wamnt:
                a.data-=wmnt
                bal-=wmnt
                ch=bool(input("do you wish to continue for an another transaction"))
                if ch==True:
                    check()
                else:
                    return
    


                    
        
    
    
            
                


