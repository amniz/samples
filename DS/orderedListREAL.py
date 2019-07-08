from Linkedlist import Linkedlist
f=open("abcnum.txt",'r')
data=f.readlines()
s1=[]
for i in data:
    lines=i.split()
    s1.extend(lines)
r=0
s=[]
for j in s1:
    k=int(j)
    s.insert(r,k)
    r+=1
sor=sorted(s)
l=Linkedlist()
for i in sor:
    l.add(i)
l.display()
n=int(input("enter the element"))
if l.search(n)==True:
    l.remove(n)
    l.display()
else:
    g=l.searchpos(n)
    l.insert(g,n)
    l.display()
    
    
##def check(l):
##    
##    if l.search(n)==True:
##        l.remove(n)
##    else:
##        h=l.size()
##        while h>0:
##            k=l.self.first
##            
##class orderedlist:
##
##   def __init__(self):
##       self.ob=Linkedlist()
##   def adding(self,s):
##       m=sorted(s)
##       for j in m:
##           Linkedlist.add(self.ob,j)
##       self.ob.display()
##
##   def check(self,n):
##       if Linkedlist.search(self.ob,n)==True:
##           Linkedlist.remove(self.ob,n)
##       else:
##           Linkedlist.add(self.ob,n)
##       self.ob.display()
##a=orderedlist()
##a.adding(s)
##n=int(input("enter the number"))
##a.check(n)






