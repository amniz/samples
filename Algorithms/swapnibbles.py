#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:i. Swap nibbles and find the new number.
	  #ii. Find the resultant number is the number is a power of 2. 

from Algorithms.util import util
number=util.tobinary(int(input("enter the number number to be swapped")))#calling tobinary function to change the number to binary
print("binary value before swap",number)
j=1
i=0
final_string=str()
m=0
while m<4:#running loop till 32 bits
    j=0
    while j<4:#traversing the first 4 bit
        final_string+=number[i+4]
        j+=1
        i+=1
    while j<8:#going back and changing the values of first 4 bits
        final_string+=number[i-4]
        j+=1
        i+=1
    m+=1
print("binary value  after swap ",final_string)
limit_value=31
sum=int()
for i in final_string:
    #print(i)
    if i=='1':#getting the decimal equalent of the swapped number
        sum+=2**limit_value
        limit_value-=1
    else:
        limit_value-=1
print("equivalent binary value is ",sum)
    
    
        
    
