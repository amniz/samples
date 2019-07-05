#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose: find the roots of the equation a*x*x + b*x + c
import math
str1=input("enter the equation")
list1=str1.split('+')
q=list1[0]
w=q.split('x2')
a=int(w[0])

q1=list1[1]
w1=q1.split('x')
b=int(w1[0])

c=int(list1[2])
print (a,b,c)

delta = b*b - 4*a*c
print(delta)
k=math.sqrt(delta)
Root1 = (-b + k)/(2*a)
Root2 = (-b - k)/(2*a)
print(Root1)
print(Root2)
