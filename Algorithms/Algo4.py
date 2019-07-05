import util
import time
a=[1,2,3,4,5]
arr=[2,1,4,6,3]
h=len(a)
l=0
k=4
tbs=time.time()
util.util.BinarySearch(a,h,l,k)
tbs1=time.time()
print(tbs1-tbs)
tbs=time.time()
util.util.Insertionsort(arr)
tbs1=time.time()
print("time elapsed by insertion sort",tbs1-tbs)
tbs=time.time()
util.util.Insertionsort(arr)
tbs1=time.time()
print("time elapsed by bubble sort",tbs1-tbs)
