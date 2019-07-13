#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:A program with cubic running time. Read in N integers and counts the number of triples that sum to exactly 0. 
try:
	n=int(input("enter the number of elements"))
except ValueError:
	n=int(input("please do enter the integer elements"))
li=[]
m=[]

while(n>0):
    li.append(int(input("enter the elmnt")))
    n-=1
for i in li:#checking for the triplets which sum to zero
    for j in li:
        for k in li:
            if i+j+k==0:#if triplets sum is zero then adding the elements
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
sett=set(m)#avoiding the duplicate elements
print (sett)
print("distict triplets are",len(sett))
                
                
    
