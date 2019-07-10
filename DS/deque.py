#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose: checks whether a string is palindrome or not by using deque
class Dnode:
    def __init__(self, data=None, nexp=None, prev=None):
        self.data = data
        self.nexp = nexp
        self.prev = prev


class Deque:
    def __init__(self):
        self.dq = Dnode()
        self.count = 0

    def addFront(self, data):
        if self.count == 0:
            print("adding initial data", data)
            self.dq.data = data
            self.count += 1
        else:
            print("init add",self.dq)
            first = self.dq
            while first.prev != None:
                first = first.prev
            print("adding data", data)
            first.prev = Dnode(data, first, None)
            self.dq=first.prev
            print("last add", self.dq)
            #print(self.dq.nexp.data)
    def addRear(self, data):
        if self.count == 0:
            self.dq.data = data
            self.count += 1
        else:
            first = self.dq
            while first.nexp != None:
                first = first.nexp
            first.nexp = Dnode(data, None, first)
            self.count += 1


    def removeFront(self):
        print("infront")
        if self.count == 0:
            return self.dq.data
        else:
            first = self.dq
            print("firstrera",first.data)
            c = 1
            while first.prev != None:
                first = first.prev
                c += 1
            temp = self.dq
            while c > 2:
                temp = temp.prev
                c -= 1
            dat=temp.data
            temp.prev = None
            self.count -= 1
            print("frontdat",dat)


    def removeRear(self):
        print("in rear")
        if self.count == 0:
            return self.dq.data
        else:
            last = self.dq
            k = 1
            while last.nexp != None:
                last = last.nexp
                k += 1
            temp = self.dq

            while k > 1:

                temp = temp.nexp
                k-=1
            dat=temp.data
            temp.nexp = None
            self.count -= 1


    def isEmpty(self):
        if self.count == 0:
            return True
        else:
            return False

    def size(self):
        return self.count

    def display(self):
        last = self.dq
        while last.prev != None:
            last = last.prev
        while last.nexp != None:
            print(last.data)
            last = last.nexp
        print(last.data)


def main():
    q = Deque()
    l = Deque()
    s = input("enter the string")
    for i in s:
        print("ooi", i)
        q.addFront(i)
        l.addRear(i)
    q.display()
    l.display()
    le = l.size()
    print(le)
    q1=q.dq.data
    l1=l.dq.data
    while le > 0:
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
    if le<=2:
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


if __name__ == '__main__':
    main()
            
        
        
                
                
