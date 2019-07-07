import array
class stack:
    def __init__(self):
        self.arr=array.array('u',"")
        self.data=[input("enter the eqation")]
        self.count=0
    def push(self,data):
        print("called push")
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
        print(type(j))
        print(j)
        ke=0
        print(j[0][0])
        for i in j:
            print("i",i)
            print(type(i))
            m=0
            while m<len(i):
                print(m,"m")
                print(len(i))
                print("inside")
                print
                if i[ke]=='(':
                    print("olakka")
                    self.push('(')
                    ke+=1
                    m+=1
                elif i[ke]==')':
                    pop('(')
                    ke+=1
                    m+=1
                m+=1
                ke+1
        print(self.isempty())
a=stack()
a.check()
        
    
        
