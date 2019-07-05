from util import util
with open("abc.txt","r") as file:
    d=file.readlines()
    g=[]
    for x in d:
        line=x.split()
        g.extend(line)
    util.Insertionsort(g)
    print(g)
s=input("enter the word to be searched")
util.BinarySearch(g,len(g),0,s)

