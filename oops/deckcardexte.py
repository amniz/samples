#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:implementation of queue using linked list
from oops.DeckofCards import deckofcard

# creating node class
class Node:
    def __init__(self,data=None,nexp=None):
        self.data=data # data attribute
        self.nexp=nexp # next pointer attribute

class Queue:
    def __init__(self):
        self.first=Node()#creating the node
        self.count=0
    def add(self,data):#adding elements to the node
        if self.first.data==None:
            self.first.data=data
            self.first.nexp=None
            self.count+=1
        else:
            last=self.first
            while last.nexp!=None:
                last=last.nexp
            last.nexp=Node(data,None)
            self.count+=1
    def pop(self):#removing first element from the queue
        first=self.first.nexp
        self.first=first
        self.count-=1

    def display(self): # displaying the elements in the queue
        l=self.first
        while l.nexp!=None:
            print(l.data)
            l=l.nexp
        print(l.data)
class player:
    @staticmethod
    def sort(cards):
        print("olakka")
        if 'Ace' in cards:
            return 5
        elif  'king' in cards:
            return 4
        elif 'Queen' in cards:
            return 3
        elif "Jack":
            return 2
        else:
            return 1

    def palyer(self):
        print("hai")
        cards=deckofcard()
        cards.sort(key=self.sort)
        print(cards)
def main():
    c=player()
    c.palyer()
if __name__=="__main__":
    main()


