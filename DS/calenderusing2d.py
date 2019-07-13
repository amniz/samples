#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose: prints the claender of a given date using a 2d array.
from util import util
import sys
m=int(sys.argv[1])
y=int(sys.argv[2])
k=util.daysofWeek(m,y)
d=int(k)
go=d+9
days=[x for x in range(1,util.monthDay(m,y))]
print("     python cal",m," ",y)
print("    S   M  T   W  Th   F   S")
li=[]
val=42
c=0
while val>0:
    g=[]
    n=0

    while n<=6:
        while d>0:
            g.append(" ")
            n+=1
            val-=1
            d-=1
        try:
            g.append(days[c])
            c+=1
            n+=1
            val-=1
        except:
            g.append(" ")
            c+=1
            n+=1
            val-=1
    li.append(g)

for k in li:

    n=0
    while n<=6:
        if go>0:
            print("  ",k[n],end="")
            n+=1
            go-=1
        else:
            print(" ",k[n],end="")
            n+=1
    print()
