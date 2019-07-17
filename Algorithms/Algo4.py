#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:Check using Stopwatch the Elapsed Time for every method call
from Algorithms.util import util
import time

array_for_binarysearch=[1,2,3,4,5]
unsorted_list=[2,1,4,6,3]
last_element=len(array_for_binarysearch)
first_element=0
key=4
start_time=time.time()#getting the time since epoch
util.BinarySearch(array_for_binarysearch,last_element,first_element,key)
end_time=time.time()#getting the time since epoch
print("timpe elapsed by binary search",end_time-start_time)#substracting both the time and finding the time elapsed
start_time=time.time()#getting the time since epoch
util.Insertionsort(unsorted_list)
end_time=time.time()#getting the time since epoch
print("time elapsed by insertion sort",end_time-start_time)
start_time=time.time()#getting the time since epoch
util.Insertionsort(unsorted_list)
end_time=time.time()#getting the time since epoch
print("time elapsed by bubble sort",end_time-start_time)
