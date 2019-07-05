#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:A program with cubic running time. Read in N integers and counts the number of triples that sum to exactly 0. 

n=int(input("enter the number of elements"))
li=[]
m=[]

while(n>0):
    li.append(int(input("enter the elmnt")))
    n-=1
for i in li:
    for j in li:
        for k in li:
            if i+j+k==0:
                count=0
                
                g=[]
                g.append(i)
                g.append(j)
                g.append(k)
                p=tuple(g)
                
                m.insert(count,p)
                #print(i,j,k)
            else:
                continue
sett=set(m)
print (sett)
print("distict triplets are",len(sett))
                
                
    
