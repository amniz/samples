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
    
