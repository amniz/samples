#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:> Read in a list of words from File. Then prompt the user to enter a word to
#search the list. The program reports if the search word is found in the list.
from util import util#importing from util
with open("abc.txt","r") as file:#reading the file
    d=file.readlines()
    g=[]
    for x in d:
        line=x.split()
        g.extend(line)#splitting ti each word
    util.Insertionsort(g)#sorting the words using insertion sort
    print(g)
s=input("enter the word to be searched")
util.BinarySearch(g,len(g),0,s)#searching the word using binary search

