#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:Given N distinct Coupon Numbers, how many random numbers do you need to generate distinct coupon number? This program simulates this random process. 
import random
n=int(input("give the number of coupons to be generated"))
s="0qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
#print(s.length)
#max=1000
#print(len(s))

fin=set()
while n>0:
        coupon=""
        print("n",n)
        max1=10000
        while max1>0:
            rand=int(random.uniform(1,62))
            print(rand)
            coupon+=s[rand]
            max1=int(max1/rand)
            print(coupon)
        fin.add(coupon)
        n-=1
print(fin)
