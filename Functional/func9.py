#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:A library for reading in 2D arrays of integers, doubles, or booleans from standard input and printing them out to standard output


n=int(input("enter 1->boolean 2->integer 3->float"))

row=int(input("enter the number of rows"))
col=int(input("enter the number of columns"))
a=[]
def Boolea(row,col):
    while(row>0):
        b=[]
        col1=col
        while(col1>0):
            n=bool(input("enter the \row \col element"))
            b.append(n)
            col1-=1
        a.append(list(b))
        row-=1
    print(a)
        
def Inte(row,col):
    while(row>0):
        b=[]
        col1=col
        while(col1>0):
            n=int(input("enter the \row \col element"))
            b.append(n)
            col1-=1
        a.append(list(b))
        row-=1
    print(a)
def Floa(row,col):
    while(row>0):
        b=[]
        col1=col
        while(col1>0):
            n=float(input("enter the \row \col element"))
            b.append(n)
            col1-=1
        a.append(list(b))
        row-=1
    print(a)
if n==1:
    Boolea(row,col)
elif n==2:
    Inte(row,col)
elif n==3:
    Floa(row,col)
else:
    print("sorry wrong option")
    exit()

