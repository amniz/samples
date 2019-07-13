#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose: Simulates a gambler who start with $stake and place fair $1 bets until he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of times he/she wins and the number of bets he/she makes. Run the experiment N times, averages the results, and prints them out


import random#random module for generating random numbers
from util import gambler
stake=int(input("enter the stake"))
goal=int(input("enter teh goal"))
time=int(input("enter the number of times"))
gambler(stake,goal,time)
