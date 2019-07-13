#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:Computes the prime factorization of N using brute force. 

try:
	n=int(input("enter the number to find the prime factors"))
except ValueError:
	n=int(input("please do enter an integer value"))
	

i=2
while i*i<=n:
    t=2
    while t<=i:
        if n%t==0:
            k=1


            
           # if k==t:
            #    print("in k")
             #   i+=1
              #  break
            #elif k<t:
            while k<t:
                    if t%k==0:
                        #i+=1
                        t+=1
                        break
                    else:
                        print(t)
                        i+=1
                        t+=1
            #else:
               # break
        else:
            t+=1
            i+=1
            break
            
