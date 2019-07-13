import random
import math
def randmgen(n):
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
    return head,tail
def leapyear(n):

        if n%400==0:#checking whether divisble by 400
            return "its a leap year"
        elif n%100==0:#checking whether divisble by 100
            return "its not a leap year"
        elif n%4==0:#checking whether divisble by 4
            return "its a leap year"
        else:
            return "not a leap year"
def twopow(n,t):
    if n>31 or n<0:#ensuring the number is between 0 and 31
        print("over flow")
    else:
        while (t>0):
            print(t,end="")
            print(leapyear(t))
            print(end="\n")
            t=int(t/2)
def harmon(n):
    t=1
    sum=0
    while(t<=n):#generating and printing the harmonic number
        sum=1/t

        print("1/",t,"=",1/t)
        t+=1
    return sum
def gambler(stake,goal,time):

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
                #print("won")
            else:#generating loss
                s-=1
                loss+=1
                #print("loss")
        time-=1
        print(time,"win",win/count)#calculating win
        print(time,"loss",loss/count)#calculating loss
def coupon(n):

    s="0qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"#for generating random numbers
    #print(s.length)
    #max=1000
    #print(len(s))

    fin=set()#avoiding duplicate elements
    while n>0:#generating random numbers n number of times
            coupon=""
            #print("n",n)
            max1=10000
            while max1>0:#generating random number
                rand=int(random.uniform(1,62))#generating a random number between 1 and 62
                #print(rand)
                coupon+=s[rand]#appending the character to the string
                max1=int(max1/rand)
                #print(coupon)
            fin.add(coupon)#adding the coupon
            n-=1
    return fin
def Boolea(row,col):#function to generate boolean array
    a=[]
    while(row>0):#entering the elementts to the row
        b=[]
        col1=col
        while(col1>0):#entering the elements to the column
            n=bool(input("enter the \row \col element"))
            b.append(n)
            col1-=1
        a.append(list(b))#adding the particular element
        row-=1
    print(a)

def Inte(row,col):#function to generate integer array
    a=[]
    while(row>0):#entering the elementts to the row
        b=[]
        col1=col
        while(col1>0):#entering the elements to the column
            n=int(input("enter the \row \col element"))
            b.append(n)
            col1-=1
        a.append(list(b))
        row-=1
    print(a)
def Floa(row,col):#function to generate double array
    a=[]
    while(row>0):#entering the elementts to the row
        b=[]
        col1=col
        while(col1>0):#entering the elements to the column
            n=float(input("enter the \row \col element"))
            b.append(n)
            col1-=1
        a.append(list(b))#adding the particular element
        row-=1
    print(a)
def triplets(n):
    li=[]
    m=[]

    while(n>0):
        li.append(int(input("enter the elmnt")))
        n-=1
    for i in li:#checking for the triplets which sum to zero
        for j in li:
            for k in li:
                if i+j+k==0:#if triplets sum is zero then adding the elements
                    count=0

                    g=[]
                    g.append(i)
                    g.append(j)
                    g.append(k)
                    p=tuple(g)

                    m.insert(count,p)
                    #print(i,j,k)
                else:
                    continue
    sett=set(m)#avoiding the duplicate elements
    return sett
def dist(n,n1):
    distance=math.sqrt(n**n+n1**n1)#calculating using the formula
    return distance
def check(l,n):#checking for the winner
    #print("id of l in check",id(l))
    hum=0
    comp=0
    for i in range(3):
        for j in range (1):#checking through the rows human
            if l[i][j]=='x' and l[i][j+1]=='x' and l[i][j+2]=='x':
                hum+=1
    for i in range(3):#checking through the row for comp
        for j in range (1):
            if l[i][j]=='o' and l[i][j+1]=='o' and l[i][j+2]=='o':
                comp+=1
    for i in range(1):#checking through the column for human
        for j in range (3):
            if l[i][j]=='x' and l[i+1][j]=='x' and l[i+2][j]=='x':
                hum+=1
    for i in range(1):#checking through the column for comp
        for j in range (3):
            if l[i][j]=='o' and l[i+1][j]=='o' and l[i+2][j]=='o':
                comp+=1
    if l[0][0]=='x' and l[1][1]=='x' and l[2][2] =='x' or l[0][2]=='x' and l[1][1]=='x' and l[2][1]=='x':
        hum+=1#checking through the diagonal for human
    if l[0][0]=='o' and l[1][1]=='o' and l[2][2] =='o' or l[0][2]=='o' and l[1][1]=='o' and l[2][1]=='o':
        comp+=1#checking through the diagonal for comp
    if comp or hum==1 and n<3:#checking for the winner
        if hum>comp:
            print("human wins")
        elif comp>hum:
            print("comp wins")
        else:
            print("match draw")
def disptic(li):#displaying the elements
    print("id of li in disp",id(li))
    for i in range(0,len(li)):
        j=0
        while j<3:
            print(li[i][j],"|",end='')
            j+=1
        print()
def windchil(t,v):
    if t<50 and v<120 and v>3:#using formula and calculating necessary
        w=35.74+(0.6215*t)+((0.4275*t)-35.75)*v**0.16
        return w
    else:
        return "cabnnot be calculated"
