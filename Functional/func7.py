#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose: Simulates a gambler who start with $stake and place fair $1 bets until he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of times he/she wins and the number of bets he/she makes. Run the experiment N times, averages the results, and prints them out



from Functional.util import gambler
stake=int(input("enter the stake"))
goal=int(input("enter the goal"))
if stake>goal:
    print("goal should be greater than stake")
    raise Exception
time=int(input("enter the number of times"))
gambler(stake,goal,time)
