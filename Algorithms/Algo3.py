#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:Program to find prime numbers that are Anagram and Palindrome 

from util import util

l1=util.isPrime()
set1=set()
set2=set()
def rev(l):
    for i in l:
        
        j=i
        val=0
        while j>0:
            
            rem=j%10
            
            val=val*10+rem
            
            j=j//10
            
        set1.add(val)
def rev1(l):
    
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