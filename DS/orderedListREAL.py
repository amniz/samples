#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:Read .a List of Numbers from a file and arrange it ascending Order in a
#Linked List. Take user input for a number, if found then pop the number out of the
#list else insert the number in appropriate position
from Linkedlist import Linkedlist
try:
    f=open("abcnum.txt",'r')#trying to read from the file
    data=f.readlines()
except:
    f=open("abcnum.txt",'w')#craeting the new file if not present
    data=f.write("1,2,3,4,5")
finally:
    f.close()
s1=[]
for i in data:#getting the data from the file
    lines=i.split()
    s1.extend(lines)
r=0
s=[]
for j in s1:
    k=int(j)
    s.insert(r,k)#parsing and inserting
    r+=1
sor=sorted(s)#sorting the list
l=Linkedlist()
for i in sor:
    l.add(i)#adding the elements
l.display()
n=int(input("enter the element"))
if l.search(n)==True:
    l.remove(n)#removing the element if found
    l.display()
else:
    g=l.searchpos(n)
    l.insert(g,n)#inserting the element if not found in the appropriate position
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
