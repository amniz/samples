#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose: Flip Coin and print percentage of Heads and Tails
from Functional.util import randmgen
try:#ensuring the person enters a number
	n=int(input("enter the number of times you need to flip the coin"))
except ValueError:
	n=int(input("enter an integer"))
h,t=randmgen(n)
print("percent is",(h/t)*100)#printing the percentage of heads and tails
