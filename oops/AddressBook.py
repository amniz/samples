class Person:#person class for each element in the address book
    def __init__(self):
        self.first=input("enter the first name")#creating and inituializing person
        self.last=input("enter the last name")
        self.address=input("enter the address")
        self.city=input("enter the city")
        self.state=input("enter the state")
        try:
            self.zip=int(input("enter the zip"))
            self.phonenumber=int(input("enter the phonenumber"))
        except:
            print("sorry invalid data")
class AddressBook:#creating a class address book
    def __init__(self):
        self.page=[Person()]#adddress book has a person
        # self.nexp=None
        # self.count=0
    def add(self):#adding a person to the address book
        # if self.count==0:
        #     self.nexp=None
        # else:
        #     first=self
        #     while first.nexp!=None:
        #         first=first.nexp
        #     first.nexp=Person()
        #     first.count-=1
        self.page.append(Person())
    def display(self):
        for i in range(len(self.page)):
            print("firstname",self.page[i].first)
            print("lastname",self.page[i].last)
            print("address",self.page[i].address)
            print("city",self.page[i].city)
            print("state",self.page[i].state)
            print("zip",self.page[i].zip)
            print("phno",self.page[i].phonenumber)

    def edit(self):#editing the details of the person in the address book
        fname=input("enter the first name of the person")
        lname=input("enter the lname of the person")
        leofp=len(self.page)
        i=0
        while leofp>0:


            if self.page[i].first==fname and self.page[i].last==lname:
                ed=int(input("enter the option you need to edit 1->address\n2->city\n3->state\n4->zip\n5->phonenumber"))
                if ed==1:
                    self.page[i].address=input("enter the new address and press enter")
                    wis=int(input("1->anymore edit\n2->quit"))
                    if wis==1:
                        self.edit()
                    elif wis==2:
                        print("update done successfully")
                        return
                    else:
                        print("not a valid option")
                elif ed==2:
                    self.page[i].city = input("enter the new city and press enter")
                    wis = int(input("1->anymore edit\n2->quit"))
                    if wis == 1:
                        self.edit()
                    elif wis == 2:
                        print("update done successfully")
                        return
                    else:
                        print("not a valid option")
                elif ed==3:
                    self.page[i].state = input("enter the new state and press enter")
                    wis = int(input("1->anymore edit\n2->quit"))
                    if wis == 1:
                        self.edit()
                    elif wis == 2:
                        print("update done successfully")
                        return
                    else:
                        print("not a valid option")
                elif ed==4:
                    self.page[i].zip = input("enter the new zip and press enter")
                    wis = int(input("1->anymore edit\n2->quit"))
                    if wis == 1:
                        self.edit()
                    elif wis == 2:
                        print("update done successfully")
                        return
                    else:
                        print("not a valid option")
                elif ed==5:
                    self.page[i].phonenumber= input("enter the new phonenumber and press enter")
                    wis = int(input("1->anymore edit\n2->quit"))
                    if wis == 1:
                        self.edit()
                    elif wis == 2:
                        print("update done successfully")
                        return
                    else:
                        print("not a valid option")
            leofp-=1
            i+=1
    def delete(self):
        fname = input("enter the first name of the person")
        lname = input("enter the lname of the person")
        leofp = len(self.page)
        print(leofp)
        i = 0
        while leofp>1:
            print(leofp)
            print(i)
            if self.page[i].first == fname and self.page[i].last == lname:
                self.page.remove(self.page[i])
            i+=1
            leofp-=1
    # @staticmethod
    # def takelname(self,i):
    #     return self.page[i].last

    def sort(self):
        n=int(input("select by which category it need to be sorted\n 1->lastname\n2->zipcode"))
        i=0
        leofp=len(self.page)
        while leofp>1:
            if n==1:
                self.page.sort(key = lambda Person:Person.last)
            elif n==2:
                self.page.sort(key=lambda Person:Person.zip)
            leofp-=1
            i+=1



n=int(input("enter the number of"))
a = AddressBook()
for i in range(n):
    a.add()
a.display()
a.sort()
a.display()


