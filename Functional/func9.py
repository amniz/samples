#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:A library for reading in 2D arrays of integers, doubles, or booleans from standard input and printing them out to standard output
from Functional.util import Boolean_array,Integer_array,Float_array
try:
	user_selection=int(input("enter 1->boolean 2->integer 3->float"))
except ValueError as e:
	print("please do select one of these option",e)

try:
    row=int(input("enter the number of rows"))#getting number of rows
    col=int(input("enter the number of columns"))#getting number of columns
except ValueError as e:
    print("enter a integer value",e)



if user_selection==1:#getting the input from the user and checking it
    Boolean_array(row,col)
elif user_selection==2:
    Integer_array(row,col)
elif user_selection==3:
    Float_array(row,col)
else:
    print("sorry wrong option")
    
