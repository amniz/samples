#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:Find the Fewest Notes to be returned for Vending Machine
from util import util
n=int(input("enter the change"))
count=int()
coins=(1,2,5,10,50,100,500,1000)
g=len(coins)-1


util.check1(n,count,coins,g)
