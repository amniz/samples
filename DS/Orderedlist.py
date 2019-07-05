import Linkedlist
f=open("abc.txt","r")
d=f.readlines()
g=[]
for x in d:
    line=x.split()
    g.extend(line)


l=Linkedlist.Linkedlist()
m=Linkedlist.Linkedlist()
n=input("enter the word to be searched for")
flag=False

for i in g:
    Linkedlist.Linkedlist.add(l,i)
l.display()
sil=Linkedlist.Linkedlist.size(l)
t=l
if Linkedlist.Linkedlist.search(t,n)==True:
    m=Linkedlist.Linkedlist.remove(t,n)


else:
    print("element not found adding the element")
    Linkedlist.Linkedlist.add(l,n)
m.display()



