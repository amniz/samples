#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose: Flip Coin and print percentage of Heads and Tails
from Functional.util import random_number_generator
try:#ensuring the person enters a number
	coin_flip_times=int(input("enter the number of times you need to flip the coin"))
except ValueError as e:
	print("enter an Integer value",e)
head,tails=random_number_generator(coin_flip_times)
print("Number of heads is",head)
print("Number of tails is",tails)
print("percent of head/tail is ",(head/tails)*100)#printing the percentage of heads and tails
