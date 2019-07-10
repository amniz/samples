#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose: prime numbers in the range of 0-1000 using 2d array
def isPrime(min,max):
        l=[]
        #n=int(input("enter the number "))
        for i in range(min,max):
                
                if i==2:
                    l.append(i)
                else:
                    j=2
                    while(j<=i):
                        if i%j==0:
                            break
                       
                        else:
                            j+=1


                    if j==i:
                        l.append(i)
        return l
r=[]
for i in range(0,1000,100):
    k=isPrime(i,i+100)
    r.append(k)
h=0
for i in range(0,1000,100):
    
    print("prime numbers in the range of",i,"and",i+100,":",end="")
    print(r[h])
    h+=1
