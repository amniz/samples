#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose: Read the Text from a file, split it into words and arrange it as Linked List.
#Take a user input to search a Word in the List. If the Word is not found then add it
#to the list, and if it found then remove the word from the List. In the end save the
#list into a file.
from Linkedlist import Linkedlist
f=open("abc.txt","r")
d=f.readlines()
g=[]
for x in d:
    line=x.split()
    g.extend(line)


l=Linkedlist()
m=Linkedlist()
n=input("enter the word to be searched for")
flag=False

for i in g:
    l.add(i)
l.display()
print("init",l.size())
sil=l.size()
t=l
if l.search(n)==True:
    l.remove(n)


else:
    print("element not found adding the element")
    l.add(n)
    l.display()
l.display()
print("last",l.size())


