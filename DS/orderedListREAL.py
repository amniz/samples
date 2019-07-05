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
class orderedlist:

   def __init__(self):
       self.ob=Linkedlist()
   def adding(self,s):
       for j in s:
           Linkedlist.add(self.ob,j)
       self.ob.display()

   def check(self,n):
       if Linkedlist.search(self.ob,n)==True:
           Linkedlist.remove(self.ob,n)
       else:
           Linkedlist.add(self.ob,n)
       self.ob.display()
a=orderedlist()
a.adding(s)
n=int(input("enter the number"))
a.check(n)






