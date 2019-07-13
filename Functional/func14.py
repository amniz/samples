
#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:TicTacToe
import random
from Functional.util import check,disptic
li=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]#creating an empty list

#print("id of li in normal",id(li))




n=9
while n>0:#playing the game
    if n%2!=0:#chance for human
        try:
            row=int(input("enter the value row"))#selecting row by human
            col=int(input("enter the value of col"))#selecting column by human
        except IndexError as e:
            print("in except",e)
            row=int(input("enter the value row"))#selecting row by human
            col=int(input("enter the value of col"))#selecting column by human
        if li[row][col]==' ':
            print("hum sel",row," ",col)
            li[row][col]='x'
            n-=1
            disptic(li)#dispalying theelements
                #check(li,n)
        else:
            print("its already selected enter another one")
    else:#chance for comp
        row=random.randint(0,2)#selecting row by comp
        col=random.randint(0,2)#selecting column by comp
        if li[row][col]==' ':
            print("comp sel",row," ",col)
            li[row][col]='o'
            n-=1
            #check(li,n)
        else:
            continue

check(li,n)
