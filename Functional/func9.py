#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:A library for reading in 2D arrays of integers, doubles, or booleans from standard input and printing them out to standard output

try:
	n=int(input("enter 1->boolean 2->integer 3->float"))
except ValueError:
	print("please do select one of these option")
	n=int(input("enter 1->boolean 2->integer 3->float"))

row=int(input("enter the number of rows"))#getting number of rows
col=int(input("enter the number of columns"))#getting number of columns
a=[]
from util import Boolea,Inte,Floa

if n==1:#getting the input from the user and checking it
    Boolea(row,col)
elif n==2:
    Inte(row,col)
elif n==3:
    Floa(row,col)
else:
    print("sorry wrong option")
    
