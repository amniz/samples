#@author:Muhammed Nisamudheen
#@version:python 3.7
#purpose:Implementing Linked List with different methods

class Node:          #Node classs for storing data of the node
    def __init__(self,data=None,nexp=None):
        self.data=data
        self.nexp=nexp
class Linkedlist:      #Linked list class key purpose is to make an object of this class and the make an object and travesrse and add the neccesary xdata element of the Linked list through this object
    def __init__(self):
        self.first=Node()
        print("self.first initially",self.first)
        self.count=0
    # def __iter__(self):
    #     self.i=0
    #     return self
    # def __next__(self):
    #     temp=self.first.data
    #     while self.i<self.count:
    #         print (temp.data)
    #         temp=temp.nexp
    #         self.i+=1

    def add(self,data):      #for adding data to the linked list
        if self.first.data==None:
            self.first.data=data
            self.first.nexp=None
            self.count+=1
        else:
            last=self.first     #making a temporary variable for traversal and insertion purposes
            while last.nexp!=None:     #looping to find out the last node
                last=last.nexp
            last.nexp=Node(data,None)
            self.count+=1
    def remove(self,data):#removes the specific element from the list
        print("in remove")

        if self.first.data==data:#if the element is the first element removing it
            self.first=self.first.nexp
            self.count-=1
        else:#if the element is some other element rather than the first element
            c=1
            last=self.first
            temp=self.first
            while last.nexp!=None:
                last=last.nexp
                c+=1
                if last.data==data:
                    temp.nexp=last.nexp
                    self.count-=1
                    return
                temp=temp.nexp


    def pop(self):#removes the last element of the linkedlist
        last=self.first
        n=self.count
        while n>2:#loop to go till the element before the last element
            last=last.nexp
            n-=1
        last.nexp=None
    def search(self,data):#searches an element in the linked list and return whether the element is present in the linked list or not
        co=0
        while self.first.nexp!=None:#checking till the element before the last element
            if self.first.data==data:
                break
            else:
                co+=1
                self.first=self.first.nexp
        if self.first.data==data:#checking the last element is the given data
            return True
        if co<=self.count-2:
           return True
        else:
           return False

    def isEmpty(self):#return the list empty or not
        if self.count==0:
            return True
        else:
            return False
    def append(self,data):#inserts the given element to the end of the linked list
        last=self.first
        while last.nexp!=None:
            last=last.nexp
        last.nexp=Node(data,None)
        self.count+=1
    def index(self,data):#returns the index of the specific element in the list
        last=self.first
        co=0
        while last.nexp!=None:
            co+=1
            if last.data==data:
                return co
            else:
                last=last.nexp
        if last.data==data:
            return self.count
        else:
            return "sorry the element is not found in the list"
    def insert(self,pos,data):#insert the element in the sepecfied postion
        last=self.first
        if pos==1:#if the element to be inserted is at the first position
            last=Node(data,self.first)
            self.count+=1
            self.first=last
            return
        else:#if the element is to be inserted somewhere between first and last
            temp=self.first
            co=1
            c=1
            if pos<self.count:
                while c<pos:
                    print(c,"c")
                    print(pos,"pos")
                    c += 1
                    temp=temp.nexp
                    print("temp",temp.data)

                while co<pos-1:
                    co+=1
                    last=last.nexp
                last.nexp=Node(data,temp)
                self.count+=1
            else:#if the element is to be insreted at the last position
                while last.nexp!=None:
                    last=last.nexp
                last.nexp=Node(data,None)
    def pop(self,index):#poping at the specified position
        last=self.first
        if index==1:#poping at the first position
            self.first=self.first.nexp
            self.count-=1
            return
        elif index>1 and index<self.count:#poping at the position between first and last
            co=2
            c=2
            temp=self.first
            while c<=index:

                temp=temp.nexp
                c += 1

            while co<index:
                print("co",co)
                print("index",index)

                last=last.nexp
                co += 1

            last.nexp=temp.nexp
            self.count-=1
        else:#poping at the position of last
            i=2
            last=self.first
            while i<self.count:
                last=last.nexp
                i+=1
            last.nexp=None
            self.count-=1

    def display(self):    #display method to print all the elements in the linked list

        last=self.first
        while last.nexp!=None:

           print("element is",last.data,"nexp",last.nexp,"id is ",id(last.data))

           last=last.nexp
        print(last.data)
    def size(self):#returns the size of the linked list
        return self.count

# a=Linkedlist()
# a.add(10)
# a.add(20)
# a.add(30)
# a.add(40)
#
# a.display()
# #a.pop()
# #a.display()
# #a.pop(4)
# a.remove(20)
# a.display()
# #print(a.size())

