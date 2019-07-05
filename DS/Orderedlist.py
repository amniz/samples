import Linkedlist
f=open("abc.txt","r")
d=f.readlines()
g=[]
for x in d:
    line=x.split()
    g.extend(line)

l=Linkedlist.Linkedlist()
n=input("enter the word to be searched for")
flag=False

for i in g:
    Linkedlist.Linkedlist.add(l,i)
sil=Linkedlist.Linkedlist.size(l)

if Linkedlist.Linkedlist.search(l,n)==True:
    Linkedlist.Linkedlist.remove(l,n)


else:
    print("element not found adding the element")
    Linkedlist.Linkedlist.add(l,n)
Linkedlist.Linkedlist.display(l)



