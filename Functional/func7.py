#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose: Simulates a gambler who start with $stake and place fair $1 bets until he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of times he/she wins and the number of bets he/she makes. Run the experiment N times, averages the results, and prints them out


import random#random module for generating random numbers
stake=int(input("enter the stake"))
goal=int(input("enter teh goal"))
time=int(input("enter the number of times"))
while(time>0):#playing n number of times
    s=stake
    g=goal
    win=int()
    loss=int()
    count=int()
    while(s>0 and s<goal):#playing a specific game untill goal reached or stakes runs out 
        count+=1
        rand=random.random()#generating random numbers
        #print(rand)
        if rand>=0.5:#generating win
            s+=1
            win+=1
            print("won")
        else:#generating loss
            s-=1
            loss+=1
            print("loss")
    time-=1
    print(time,"win",win/count)#calculating win
    print("loss",loss/count)#calculating loss
