class util:
    def daysofWeek(mon,yea):#getting the day of the week
        m=mon
        d=1
        y=yea
        y0=int()
        x=int()
        m0=int()
        d0=int()
        y0=y-(14-m)/12#using formula and getting the value for d0
        x=y0+y0/4-y0/100+y0/400
        m0=m+12*((14-m)/12)-2
        d0=(d+x+31*m0/12)%7
        return d0
    def Leap(n):#checking whether the year is a leap year or not
        if n%400==0:#checking whether the number is divisble by 400
            return True
        elif n%100==0:#checking whether the number is divisble by 100
            return False
        elif n%4==0:#checking whether the number is divisble by 4
            return True
        else:
            return False
    def monthDay(m,y):#getting the number of days in a particular month
        i=m
        if i==2:
            if Leap(y):#checking whether the year is leap  year or not
                return 30
            else:
                return 29
        elif i in [4,6,9,11]:
            return 31
        else:
            return 32
    def isPrime(min,max):#generating prime numbers within the given range
            l=[]
            #n=int(input("enter the number "))
            for i in range(min,max):

                    if i==2:
                        l.append(i)
                    else:
                        j=2
                        while(j<=i):
                            if i%j==0:
                                break

                            else:
                                j+=1


                        if j==i:
                            l.append(i)
            return l
    def checkana(l):#checking whether the number is anagram or not
        ana=set()
        cou=0
        for i in l:
            j=str(i)
            k=sorted(j)
            for j in [x for x in l[cou+1:len(l)]]:
                h=str(j)
                m=sorted(h)
                if k==m:
                    ana.add(i)
                    ana.add(j)
            cou+=1
        return ana
