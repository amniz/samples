#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:i. Swap nibbles and find the new number.
	  #ii. Find the resultant number is the number is a power of 2. 

from toBinary import tobin
f=toBinary.tobin()
print(f)
j=1
i=0
k=str()
m=0
while m<4:
    j=0
    while j<4:
        k+=f[i+4]
        j+=1
        i+=1
    while j<8:
        k+=f[i-4]
        j+=1
        i+=1
    m+=1
print(k)
b=31
sumc=int()
for i in k:
    print(i)
    if i=='1':
        sumc+=2**b
        b-=1
    else:
        b-=1
print(sumc)
    
    
        
    
