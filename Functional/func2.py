#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose: Flip Coin and print percentage of Heads and Tails 
import random
n=int(input("enter the number of times you need to flip the coin"))
tail=0
head=0
while n>0:
    rand=random.random()
   # print(rand)
    if rand>=0.5:
        head+=1
        n-=1
    else:
        tail+=1
        n-=1
print("percent is",(head/tail)*100)
