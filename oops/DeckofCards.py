#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:Reading a message and editing it using regex
import random#importing random function
import itertools#importing itertools for cartesian product
def deckofcard():
    suit=["Clubs","Diamonds", "Hearts", "Spades"]#suit of cards
    Rank=["2", "3", "4", "5", "6", "7", "8", "9", "10","Jack", "Queen", "King", "Ace"]#rank of cards
    g=itertools.product(suit,Rank)#using product method to produce the cartesian product of the cards
    l=list(g)#converting iterttol objects to list
    random.shuffle(l)#shuffling the cards\
    # y = 1
    # li=[]
    # lis=[]
    # ki=1
    # j = 1
    # for i in range(52):
    #
    #     if j<ki*13:
    #         li.append(l[i])
    #         j+=1
    #     lis.append(li)
    #     ki+=1
    # print(li)
    #     while(y<ki*13):
    #         li.extend(l[y])
    #
    #         y+=1
    #     lis.append(li)
    #     ki+=1
    # print(lis)



#making two dimensional array necessary for printing

    i=0
    j=1
    k=1
    li=[]
    lis=[]
    #print("player", k, "card->",end="")
    while i<52:#printing the cards

        if j!=13:
            #print("inside if")
            #print(l[i],end="")
            li.append(l[i])
            i+=1
            j+=1
        else:
            j=0
            k+=1
            lis.append(li)
            li=[]
            #print()
            #print("player", k, "card->")

    return lis
cards=deckofcard()
for i in range (0,4):
    print("cards of player",i+1,"->",cards[i])