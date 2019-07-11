#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:Program to find prime numbers that are Anagram and Palindrome 

from util import util

l1=util.isPrime()#checking the number is prime or not
set1=set()
set2=set()
def rev(l):#reversing and checking for palindrome
    for i in l:
        
        j=i
        val=0
        while j>0:
            
            rem=j%10
            
            val=val*10+rem
            
            j=j//10
            
        set1.add(val)
def rev1(l):#reversing and checking for anagram
    
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
       
       
            
    

rev(l1)

rev1(set1)
print(set2)
