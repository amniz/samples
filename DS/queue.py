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
    def enqueue(self, data=None):
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

    def deque(self):
        dat = self.q.data
        self.q = self.q.nexp
        self.count -= 1
        return dat

    def isempty(self):
        if self.count == 0:
            return True
        else:
            return False

    def size(self):
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
            n = input("is there anyone on the queue")
            if n == 'True':
                self.enqueue(10)
                fw = int(input("1->deposit\n2->withdrawl"))
                if fw == 1:
                    damnt = int(input("enter the amount to be deposited"))
                    cls.bal += damnt
                    print(cls.bal)
                    self.q.data += damnt
                    print(self.q.data)
                    ch = bool(input("do you wish to continue for an another transaction"))
                    if ch == True:
                        self.check(self,cls)
                    else:
                        self.deque()
                        flag = bool(input("is anyone in the queue"))
                        if flag:
                            self.check(self,cls)
                        else:
                            return
                elif fw == 2:
                    preva=randint(100,10000)
                    self.q.data=preva
                    print(preva)
                    wamnt = int(input("enter the amount to be withdrawn"))
                    if wamnt < cls.bal - 5000 and wamnt<preva:
                        self.q.data -= wamnt
                        print(self.q.data)
                        cls.bal -= wamnt
                        ch = bool(input("do you wish to continue for an another transaction"))
                        if ch == True:
                            self.check(self,cls)
                        else:
                            self.deque()
                            flag = bool(input("is anyone in the queue"))
                            if flag:
                                self.check(self,cls)
                            else:
                                return
                    else:
                        print("transaction failed not enough bal")
            else:
                return


w = Queue()
w.check(w, Queue)

    


                    
        
    
    
            
                


