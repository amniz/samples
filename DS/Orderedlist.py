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


