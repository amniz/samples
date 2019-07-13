#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:Given N distinct Coupon Numbers, how many random numbers do you need to generate distinct coupon number? This program simulates this random process. 
import random
n=int(input("give the number of coupons to be generated"))
s="0qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"#for generating random numbers
#print(s.length)
#max=1000
#print(len(s))

fin=set()#avoiding duplicate elements
while n>0:#generating random numbers n number of times
        coupon=""
        print("n",n)
        max1=10000
        while max1>0:#generating random number
            rand=int(random.uniform(1,62))#generating a random number between 1 and 62
            print(rand)
            coupon+=s[rand]#appending the character to the string
            max1=int(max1/rand)
            print(coupon)
        fin.add(coupon)#adding the coupon 
        n-=1
print(fin)
