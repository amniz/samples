# @author:Muhammed Nisamudheen
# @version:3.7
# @purpose: Reads in integers prints them in sorted order using Bubble Sort
from Algorithms.util import util

number_of_elements = int(input("enter the total number of elements to be sorted"))
list_storing_data = []
while number_of_elements > 0:  # ensuring user gives an input
	try:
		list_storing_data.append(input("enter the element"))
	except ValueError as e:
		print("please enter valid data",e)
	number_of_elements -= 1
result = util.BubbleSort(list_storing_data)  # calling bubble sort
print("the sorted elements are",result)
