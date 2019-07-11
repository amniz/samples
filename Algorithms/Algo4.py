#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:Check using Stopwatch the Elapsed Time for every method call
import util
import time
a=[1,2,3,4,5]
arr=[2,1,4,6,3]
h=len(a)
l=0
k=4
tbs=time.time()#getting the time since epoch
util.util.BinarySearch(a,h,l,k)
tbs1=time.time()#getting the time since epoch
print(tbs1-tbs)#substracting both the time and finding the time elapsed
tbs=time.time()#getting the time since epoch
util.util.Insertionsort(arr)
tbs1=time.time()#getting the time since epoch
print("time elapsed by insertion sort",tbs1-tbs)
tbs=time.time()#getting the time since epoch
util.util.Insertionsort(arr)
tbs1=time.time()#getting the time since epoch
print("time elapsed by bubble sort",tbs1-tbs)
