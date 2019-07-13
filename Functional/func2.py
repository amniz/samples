#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose: Flip Coin and print percentage of Heads and Tails 
import random
try:
	n=int(input("enter the number of times you need to flip the coin"))
except ValueError:
	n=int(input("enter an integer"))
tail=0
head=0
while n>0:#tossing n number of times
    rand=random.random()
   # print(rand)
    if rand>=0.5:#checking for heads
        head+=1
        n-=1
    else:#checking for tails
        tail+=1
        n-=1
print("percent is",(head/tail)*100)
