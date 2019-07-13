#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:chcking for balanced aquation using stack
import array
class stack:#specifically made the stack class for checking the balanced paratnthesis
    def __init__(self):
        self.arr=array.array('u',"")#initializing the array
        self.data=[input("enter the eqation")]
        self.count=0
    def push(self,data):#pushing the elements to the array
        
        k=self.arr
        self.arr.append(data)
        self.count+=1
    def pop(self,data):#poping out the elements from the array
        j=self.arr.remove(data)
        self.count-=1
    def isempty(self):#checking whether the stack is empty or not
        if self.count==0:
            return True
        else:
            return False
    def size(self):#checking the size of the array
        return len(self.arr)
    def peak(self):#checking for the top most element
        return self.arr[0]
    def check(self):#function to push and pop the '(' from stack
        j=self.data
       
        ke=0
        
        for i in j:
            
            m=0
            while m<len(i):
                
                
                if i[m]=='(':
                    
                    self.push('(')
                    
                    ke+=1
                    m+=1
                    continue
                elif i[m]==')':
                    
                    self.pop('(')
                    ke+=1
                    m+=1
                    continue
                m+=1
                ke+1
        print("is it a balanced equation: ",self.isempty())
a=stack()
a.check()
        
    
        
