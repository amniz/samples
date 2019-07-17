#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:Given N distinct Coupon Numbers, how many random numbers do you need to generate distinct coupon number? This program simulates this random process.
import random
try:
    n=int(input("give the number of coupons to be generated"))
except:
    n=int(input("please do enter a integer"))
from Functional.util import coupon#importing coupon generator
coupon_number=coupon(n)#getting the generated coupons
print("coupons genersted are",coupon_number)
