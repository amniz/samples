#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:i. Swap nibbles and find the new number.
	  #ii. Find the resultant number is the number is a power of 2. 

from Algorithms.util import util
f=util.tobin(int(input("enter the number")))#claiing tobin function to change the number to binary
print(f)
j=1
i=0
k=str()
m=0
while m<4:#running loop till 32 bits
    j=0
    while j<4:#traversing the first 4 bit
        k+=f[i+4]
        j+=1
        i+=1
    while j<8:#going back and changing the values of first 4 bits
        k+=f[i-4]
        j+=1
        i+=1
    m+=1
print(k)
b=31
sumc=int()
for i in k:
    #print(i)
    if i=='1':#getting the decimal equalent of the swapped number
        sumc+=2**b
        b-=1
    else:
        b-=1
print(sumc)
    
    
        
    
