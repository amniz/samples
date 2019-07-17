#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:A program with cubic running time. Read in N integers and counts the number of triples that sum to exactly 0.
from Functional.util import check_triplets
try:
	element=int(input("enter the number of elements"))
except ValueError as e:
	print("enter a valid data",e)

triplets=check_triplets(element)#calling triplets function and getting the distinct value
print("distict triplets are",triplets)
print("distict triplets are",len(triplets))
