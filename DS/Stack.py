import array
class stack:
    def __init__(self):
        self.arr=array.array('u',"")
        self.data=[input("enter the eqation")]
        self.count=0
    def push(self,data):
        
        k=self.arr
        self.arr.append(data)
        self.count+=1
    def pop(self,data):
        j=self.arr.remove(data)
        self.count-=1
    def isempty(self):
        if self.count==0:
            return True
        else:
            return False
    def size(self):
        return len(self.arr)
    def peak(self):
        return self.arr[0]
    def check(self):
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
        
    
        
