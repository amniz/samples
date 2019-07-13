#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose: checks whether a string is palindrome or not by using deque
class Dnode:#creating the node class
    def __init__(self, data=None, nexp=None, prev=None):
        self.data = data#data attribute
        self.nexp = nexp#next pointer attribute
        self.prev = prev#previous pointer attribute


class Deque:
    def __init__(self):#initializing deque
        self.dq = Dnode()
        self.count = 0#counter variable

    def addFront(self, data):#adding to the front of the dequeue
        if self.count == 0:#adding to the first if the dq is empty
            print("adding initial data", data)
            self.dq.data = data
            self.count += 1
        else:
            print("init add",self.dq)
            first = self.dq
            while first.prev != None:#adding the next element
                first = first.prev
            print("adding data", data)
            first.prev = Dnode(data, first, None)#creating element at the first position
            self.dq=first.prev
            print("last add", self.dq)
            #print(self.dq.nexp.data)
    def addRear(self, data):#adding to the rear of the dequeue
        if self.count == 0:
            self.dq.data = data
            self.count += 1
        else:
            first = self.dq
            while first.nexp != None:#adding the next element
                first = first.nexp
            first.nexp = Dnode(data, None, first)#craeting element at the last position
            self.count += 1


    def removeFront(self):#removimg the element from the front from the dequeue
        print("infront")
        if self.count == 0:
            return self.dq.data
        else:
            first = self.dq
            print("firstrera",first.data)
            c = 1
            while first.prev != None:#going till the last element in the dequeue
                first = first.prev
                c += 1
            temp = self.dq
            while c > 2:#going till the element before the last element
                temp = temp.prev
                c -= 1
            dat=temp.data#deleting the last element
            temp.prev = None
            self.count -= 1
            print("frontdat",dat)


    def removeRear(self):#removing the element from the rear of the dequeue
        print("in rear")
        if self.count == 0:
            return self.dq.data
        else:
            last = self.dq
            k = 1
            while last.nexp != None:#going till the last element
                last = last.nexp
                k += 1
            temp = self.dq

            while k > 1:#traversing till the element before the last element

                temp = temp.nexp
                k-=1
            dat=temp.data#deleting the element
            temp.nexp = None
            self.count -= 1


    def isEmpty(self):#checking whether the dequeue is empty or not
        if self.count == 0:
            return True
        else:
            return False

    def size(self):#displaying the size of the deque
        return self.count

    def display(self):#displaying the elements of the dequeue
        last = self.dq
        while last.prev != None:#going to the first position
            last = last.prev
        while last.nexp != None:#displaying the element till the last element
            print(last.data)
            last = last.nexp
        print(last.data)


def main():
    q = Deque()#creating an empty deque
    l = Deque()
    s = input("enter the string")#asking the user to enter the string
    for i in s:
        print("ooi", i)
        q.addFront(i)#adding the element at the front
        l.addRear(i)#adding the element at the rear
    q.display()
    l.display()
    le = l.size()
    print(le)
    q1=q.dq.data
    l1=l.dq.data
    while le > 0:#traversing through list element by element and checking
        if q1==l1:
            #print("kooi",q.dq.data)
            #print(l.dq.data)
            #print("aa", q.dq.nexp.data)
            q1=q.dq.nexp.data

            #print("ab",l.dq.nexp.data)
            l1=l.dq.nexp.data

            le-=1
        else:
            print("in lese")
            break
    if le<=2:#checking for palindrome or not
        print("palindrome")
    else:
        print("not palindrome")
        # if q.removeRear()==l.removeFront():
        #     if le ==1:
        #         print("palindrome")
        #         break
        #     else:
        #         le-=1
        #         continue
        #
        # else:
        #     print("not palindrome")
        #     break
    # if q.size() == 0:
    #     print("palindrome")
    # else:
    #     print("Not a Palindrome")


if __name__ == '__main__':#calling main method
    main()
