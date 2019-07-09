class Node:
    def __init__(self,data=None,nexp=None,newnode=None):
        self.data=data
        self.nexp=nexp
        self.newnode=newnode
        self.nodec=0
class List:
    def __init__(self):
        self.first=Node()
        self.count=0
        self.newc=0
    def add(self,data):
        
        last=self.first
        if self.count==0:
            last=Node(data,None,None)
            self.count+=1
        else:
            while last.nexp!=None:
                last=last.nexp
            last.nexp=Node(data,None,None)
            self.count+=1
    def addele(self,data):
        print("level1")
        last=self.first
        while last.nexp!=None:
            print("level2")
            if last.data==data%11:
                print("level3")
                if last.nodec==0:
                    print("level4")
                    last.nodec+=1
                    last.newnode=Node(data,None,None)
                    print("added",data,"in",last.data)
                else:
                    while last.newNode!=None:
                        print("level5")
                        last=last.newnode
                    last.newnode(data,None,None)
                    print("added and",data,"in",last.data)
                    self.count+=1
                    last.nodec+=1
    
            last=last.nexp
                
##        last.newnode=Node(data,None,None) last element adding will be done 
##        self.count+=1
    def search(data):
        g=data%11
        last=self.first
        while last.nexp!=None:
            if last.data==g:
                if last.newnode.data==data:
                    print("found at init")
                    return
                else:
                    while last.newnode!=None:
                        if last.newnode.data==data:
                            return "found"
                    if last.newnode.data==data:
                        return "found at last"
                    else:
                        return "not found"
l=List()
for i in range(1,11):
    l.add(i%11)
f=open("abcnum.txt","r")
g=f.readlines()
gg=[]
for i in g:
    line=i.split()
    gg.extend(line)
k=[]
for j in gg:
    k.append(int(j))
print(k)
for i in range (1,11):
    l.add(i%11)
for j in k:
    print(j)
    l.addele(j)

            
