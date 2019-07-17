
#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:TicTacToe

import random
from Functional.util import check_winner,display_tic_tac_toe
empty_tic_tac_toe=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]#creating an empty list
#print("id of empty_tic_tac_toe in normal",id(empty_tic_tac_toe))
total_chances=9
while total_chances>0:#playing the game
    if total_chances%2!=0:#chance for human
        try:
            print("enter the row and column between 0 and 2")
            row=int(input("enter the value row"))#selecting row by human
            column=int(input("enter the value of column"))#selecting column by human
        except IndexError as e:
            print("in except",e)
            row=int(input("enter the value row"))#selecting row by human
            column=int(input("enter the value of column"))#selecting column by human
        if empty_tic_tac_toe[row][column]==' ':
            print("hum sel",row," ",column)
            empty_tic_tac_toe[row][column]='x'
            total_chances-=1
            display_tic_tac_toe(empty_tic_tac_toe)#dispalying theelements
                #check_winner(empty_tic_tac_toe,total_chances)
        else:
            print("its already selected enter another one")
    else:#chance for comp
        row=random.randint(0,2)#selecting row by comp
        column=random.randint(0,2)#selecting column by comp
        if empty_tic_tac_toe[row][column]==' ':
            print("comp sel",row," ",column)
            empty_tic_tac_toe[row][column]='o'
            total_chances-=1
            #check_winner(empty_tic_tac_toe,total_chances)
        else:
            continue
check_winner(empty_tic_tac_toe,total_chances)







# import random
# from Functional.util import check,disptic
# li=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]#creating an empty list
#
# #print("id of li in normal",id(li))
#
#
#
#
# n=9
# while n>0:#playing the game
#     if n%2!=0:#chance for human
#         try:
#             print("enter the row and column between 0 and 2")
#             row=int(input("enter the value row"))#selecting row by human
#             col=int(input("enter the value of col"))#selecting column by human
#         except IndexError as e:
#             print("in except",e)
#             row=int(input("enter the value row"))#selecting row by human
#             col=int(input("enter the value of col"))#selecting column by human
#         if li[row][col]==' ':
#             print("hum sel",row," ",col)
#             li[row][col]='x'
#             n-=1
#             disptic(li)#dispalying theelements
#                 #check(li,n)
#         else:
#             print("its already selected enter another one")
#     else:#chance for comp
#         row=random.randint(0,2)#selecting row by comp
#         col=random.randint(0,2)#selecting column by comp
#         if li[row][col]==' ':
#             print("comp sel",row," ",col)
#             li[row][col]='o'
#             n-=1
#             #check(li,n)
#         else:
#             continue
#
# check(li,n)
