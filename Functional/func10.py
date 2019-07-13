#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:A program with cubic running time. Read in N integers and counts the number of triples that sum to exactly 0.
try:
	n=int(input("enter the number of elements"))
except ValueError:
	n=int(input("please do enter the integer elements"))
from util import triplets
trip=triplets(n)#calling triplets function
print("distict triplets are",trip)
print("distict triplets are",len(trip))
