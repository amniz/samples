#@author:Muhammed Nisamudheen
#@version:3.7




import sys
class util:
    ####################################################################################################################
    #@purpose:Anagram Detection
    @staticmethod
    def anagram():
            str1=input("enter string 1")
            str2=input("enter string 2")
            sort1=sorted(str1)
            sort2=sorted(str2)
            if sort1==sort2:
                    print ("anagram")
            else:
                    print("not anagram")
    ######################################################################################################################
    #@purpose: Prime numbers in the range of 0 - 1000
    @staticmethod
    def isPrime():
        l=[]
        n=int(input("enter the number "))
        if n>0 and n<=1000:
            for i in range(2,n+1):

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

    #######################################################################################################################
    def rev(l):#reversing and checking for palindrome
        set1=set()
        for i in l:

            j=i
            val=0
            while j>0:

                rem=j%10

                val=val*10+rem

                j=j//10

            set1.add(val)
            return set1
    def rev1(l):#reversing and checking for anagram
        set2=set()
        for i in l:
            j=i
            val=0
            while j>0:

                rem=j%10

                val=val*10+rem

                j=j//10

            if (val==i):
                if(i>9):
                    set2.add(val)
            return set2
    #################################################################################################################################
    #@purpose: Binary Search the Word from Word List
    @staticmethod
    def BinarySearch(a,h,l,k):

        if h>=l:
            mid=int((l+h)/2)
            if a[mid]==k:
                print("mid",mid)
                return mid
            elif a[mid]>k:
                BinarySearch(a,mid-1,l,k)
            else:
                BinarySearch(a,h,mid+1,k)
        else:
            print("-1")
            return -1
    #################################################################################################################################
    #@purpose:Insertion Sort
    @staticmethod
    def Insertionsort(l):
        for i in range(1,len(l)):
            key=l[i]
            j=i-1
            while j>-1 and l[j]>key:
                l[j+1]=l[j]
                j-=1
            l[j+1]=key
    ###################################################################################################################################
    #@purpose:BubbleSort
    @staticmethod
    def Insertionsort(l):
        for i in range(1,len(l)):
            for j in range(0,len(l)-i):
                if l[j]>l[j+1]:
                    temp=l[j]
                    l[j]=l[j+1]
                    l[j+1]=temp
    #############################################################################################################################
    def daysofWeek(m,d,y):

        y0=int()
        x=int()
        m0=int()
        d0=int()
        y0=y-(14-m)/12#equating and finding out the corresponding day
        x=y0+y0/4-y0/100+y0/400
        m0=m+12*((14-m)/12)-2
        d0=(d+x+31*m0/12)%7
        if (d0==0):#checking for the corresponding day
            return "sunday"
        elif d0==1:
            return "monday"
        elif d0==2:
            return "tuesday"
        elif d0==3:
            return "wednwsday"
        elif d0==4:
            return "thursday"
        elif d0==5:
            return "friday"
        else:
            return "saturday"
    ##########################################################################
    def monthlyPayment(P,Y,R):

        n=12*Y)
        r=R/(12*100)
        pay=(P*r)/(1-(1+r)**(-n))
        return pay
###############################################################################
    def tobin(# NOTE: ):

        st=str()
        while n>=1:
            st+=str(int(n%2))
            n/=2
        e=len(st)
        while e<32:
            st+="0"
            e+=1
        t=str()
        while e>0:
            e-=1
            t+=st[e]
        return t
    ######################################################################
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
