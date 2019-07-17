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

            self.dq.data = data
            self.count += 1
        else:

            first = self.dq
            while first.prev != None:#adding the next element
                first = first.prev

            first.prev = Dnode(data, first, None)#creating element at the first position
            self.dq=first.prev

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

        if self.count == 0:
            return self.dq.data
        else:
            first = self.dq

            counter_to_delete = 1
            while first.prev != None:#going till the last element in the dequeue
                first = first.prev
                counter_to_delete += 1
            temp = self.dq
            while counter_to_delete > 2:#going till the element before the last element
                temp = temp.prev
                counter_to_delete -= 1
            dat=temp.data#deleting the last element
            temp.prev = None
            self.count -= 1



    def removeRear(self):#removing the element from the rear of the dequeue

        if self.count == 0:
            return self.dq.data
        else:
            last = self.dq
            counter_to_delete_rear = 1
            while last.nexp != None:#going till the last element
                last = last.nexp
                counter_to_delete_rear += 1
            temp = self.dq

            while counter_to_delete_rear > 1:#traversing till the element before the last element

                temp = temp.nexp
                counter_to_delete_rear-=1
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
    q_for_first_string = Deque()#creating an empty deque
    q_for_last_string = Deque()
    string = input("enter the string")#asking the user to enter the string
    for i in string:

        q_for_first_string.addFront(i)#adding the element at the front
        q_for_last_string.addRear(i)#adding the element at the rear
    q_for_first_string.display()
    q_for_last_string.display()
    size_last_string = q_for_last_string.size()

    first_string_data=q_for_first_string.dq.data
    last_string_data=q_for_last_string.dq.data
    while size_last_string > 0:#traversing through list element by element and checking
        if first_string_data==last_string_data:
            #print("kooi",q.dq.data)
            #print(l.dq.data)
            #print("aa", q.dq.nexp.data)
            first_string_data=q_for_first_string.dq.nexp.data

            #print("ab",l.dq.nexp.data)
            last_string_data=q_for_last_string.dq.nexp.data

            size_last_string-=1
        else:

            break
    if size_last_string<2:#checking for palindrome or not
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
