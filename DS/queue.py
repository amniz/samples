#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:stimulation of banking counter using queue
from random import randint
class Node:
    def __init__(self, data=None, nexp=None):
        self.data = data
        self.nexp = nexp



class Queue:
    bal = 10000000
    def __init__(self):
        self.q = Node()
        self.count = 0
    def enqueue(self, data=None):#adding the poeple into the queue
        last = self.q
        if self.count == 0:

            last.data = data
            last.nexp = None
            self.count += 1

        else:
            while last.nexp != None:
                last = last.nexp
            last.nexp = Node(data)
            self.count += 1

    def deque(self):#removing the people from the queue
        dat = self.q.data
        self.q = self.q.nexp
        self.count -= 1
        return dat

    def isempty(self):#checking whether the queue is empty
        if self.count == 0:
            return True
        else:
            return False

    def size(self):#checking the size of the queue
        return self.count

    def display(self):  # display method to print all the elements in the linked list
        if self.count == 0:
            return "no elements"
        last = self.q
        while last.nexp != None:
            print("element is", last.data, "nexp", last.nexp, "id is ", id(last.data))

            last = last.nexp
        print(last.data)
    @classmethod
    def mon(cls):
        return cls.bal

    @staticmethod
    def check(self, cls):
        flag = True
        if flag:
            n = input("is there anyone on the queue if yes type True")#checking whether ayone is there in the queue
            if n == 'True':
                self.enqueue(10)#adding the person in the queue
                fw = int(input("1->deposit\n2->withdrawl"))#checking the purpose
                if fw == 1:
                    damnt = int(input("enter the amount to be deposited"))
                    cls.bal += damnt#incrementing the bank bal
                    print("total bank balance",cls.bal)
                    self.q.data += damnt#incrementing the person bal
                    print("amount deposited",self.q.data)
                    ch = bool(input("do you wish to continue for an another transaction if yes type True"))
                    if ch == True:
                        self.check(self,cls)
                    else:
                        self.deque()
                        flag = bool(input("is anyone in the queue if yes type True"))#checking is there someone else in queue
                        if flag:
                            self.check(self,cls)
                        else:
                            return
                elif fw == 2:
                    preva=randint(100,10000)
                    self.q.data=preva
                    print("your account balance is",preva)
                    wamnt = int(input("enter the amount to be withdrawn"))
                    if wamnt < cls.bal - 5000 and wamnt<preva:#checking the amount he can with draw
                        self.q.data -= wamnt#deducting the amount from his account
                        print("your new balance is",self.q.data)
                        cls.bal -= wamnt#deducting the amount from the bank bal
                        ch = bool(input("do you wish to continue for an another transaction if yes type True"))
                        if ch == True:
                            self.check(self,cls)
                        else:
                            self.deque()
                            flag = bool(input("is anyone in the queue if yes type True"))
                            if flag:#checking is there anyone in the queue
                                self.check(self,cls)
                            else:
                                return
                    else:#failed transaction if the person doesnot have the enough balanance
                        print("transaction failed not enough balance")
            else:
                return


w = Queue()
w.check(w, Queue)
