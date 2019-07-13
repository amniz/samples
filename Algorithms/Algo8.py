#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose: Reads in integers prints them in sorted order using Bubble Sort 
from Algorithms.util import util
n=int(input("enter the number of elements"))
arr=[]
while n>0:#ensuring user gives an input
	arr.append(input("enter the element"))
	n-=1
k=util.BubbleSort(arr)#calling bubble sort
print(k)
