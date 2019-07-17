#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose: Read the Text from a file, split it into words and arrange it as Linked List.
#Take a user input to search a Word in the List. If the Word is not found then add it
#to the list, and if it found then remove the word from the List. In the end save the
#list into a file.
from DS.Linkedlist import Linkedlist
try:
    file=open("abc.txt","r")#reading from file
    d=file.readlines()
except FileNotFoundError:
    string="hai hello how are you"
    file=open("abc.txt","w")#if file not present creating a new one
    wr=file.write(string)
g=[]
for x in d:
    line=x.split()
    g.extend(line)


l=Linkedlist()#craeting a linked list object
m=Linkedlist()
n=input("enter the word to be searched for")
flag=False

for i in g:
    l.add(i)#adding the elements to the linked list
l.display()
print("init",l.size())
sil=l.size()
t=l
if l.search(n)==True:
    l.remove(n)#removing the element if found


else:
    print("element not found adding the element")
    l.add(n)#adding the eelement if not found
    l.display()
l.display()
print("last",l.size())
