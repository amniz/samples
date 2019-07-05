#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N 
n=int(input("enter the value"))
t=1
sum=0
while(t<=n):
    sum=1/t
    t+=1
    print("1/",t,"=",1/t)
print(sum)
