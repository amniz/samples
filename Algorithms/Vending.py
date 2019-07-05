#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:Find the Fewest Notes to be returned for Vending Machine 
n=int(input("enter the change"))
count=int()
coins=(1,2,5,10,50,100,500,1000)
g=len(coins)-1
def check1(n,count,coins,g):
    
    n1=n
    c=count
    k=g
    if n1==0:
        
        print("total number of coins",c)
        count
    
   
    else:
        if n1/coins[k]>=1:
            print("coins",coins[k])
            c=n1/coins[k]
            n1%=coins[k]
            print("n1",n1)
            check1(n1,c,coins,k)
            
        else:
            k-=1
            check1(n1,c,coins,k)
    
check1(n,count,coins,g)
            
