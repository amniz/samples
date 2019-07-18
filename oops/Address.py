# @author:Muhammed Nisamudheen
# @version:3.7
# @purpose:program to create a address book

# person class for each element in the address book
class Person:
    # creating and initializing person
    def __init__(self):
        self.first_name = input("enter the first_name ")
        if not self.first_name.isalpha():
            raise ValueError
        self.last_name = input("enter the last_name ")
        if not self.last_name.isalpha():
            raise ValueError
        self.address = input("enter the address")
        self.city = input("enter the city")
        if self.city.isdigit():
            raise ValueError
        self.state = input("enter the state")
        if self.state.isdigit():
            raise ValueError
        try:
            self.zip = int(input("enter the zip"))
            self.phone_number = int(input("enter the phone_number"))
        except ValueError as e:
            print("sorry invalid data", e)
            raise ValueError


# creating a class address book that stores each person data as a page in address book
class AddressBook:
    def __init__(self):
        self.page_in_addressbook = [Person()]  # address book has a person

    # adding a person to the address book
    def add(self):
        self.page_in_addressbook.append(Person())

    # method for displaying the contents of the address book
    def display_addressbook(self):
        for pages in range(len(self.page_in_addressbook)):  # displaying the elements of the address book
            print("first name", self.page_in_addressbook[pages].first_name)
            print("last name", self.page_in_addressbook[pages].last_name)
            print("address", self.page_in_addressbook[pages].address)
            print("city", self.page_in_addressbook[pages].city)
            print("state", self.page_in_addressbook[pages].state)
            print("zip", self.page_in_addressbook[pages].zip)
            print("phone number", self.page_in_addressbook[pages].phone_number)

    # editing the details of the person in the address book
    def edit_addressbook(self):
        firstname = input("enter the first_name name of the person")  # getting the necessary details for the edit
        lastname = input("enter the lastname of the person")
        length_of_addressbook = len(self.page_in_addressbook)
        counter = 0
        while length_of_addressbook > 0:  # finding the particular element
            if self.page_in_addressbook[counter].first_name == firstname and self.page_in_addressbook[
                counter].last_name == lastname:
                user_selection = int(input(
                    "enter the option you need to edit_addressbook 1->address\n2->city\n3->state\n4->zip\n5->phone_number"))
                if user_selection == 1:
                    self.page_in_addressbook[counter].address = input("enter the new address and press enter")
                    any_more_edit = int(input("1->anymore edit_addressbook\n2->quit"))
                    if any_more_edit == 1:
                        self.edit_addressbook()
                    elif any_more_edit == 2:
                        print("update done successfully")
                        return
                    else:
                        print("not a valid option")
                elif user_selection == 2:
                    self.page_in_addressbook[counter].city = input("enter the new city and press enter")
                    any_more_edit = int(input("1->anymore edit_addressbook\n2->quit"))
                    if any_more_edit == 1:
                        self.edit_addressbook()
                    elif any_more_edit == 2:
                        print("update done successfully")
                        return
                    else:
                        print("not a valid option")
                elif user_selection == 3:
                    self.page_in_addressbook[counter].state = input("enter the new state and press enter")
                    any_more_edit = int(input("1->anymore edit_addressbook\n2->quit"))
                    if any_more_edit == 1:
                        self.edit_addressbook()
                    elif any_more_edit == 2:
                        print("update done successfully")
                        return
                    else:
                        print("not a valid option")
                elif user_selection == 4:
                    self.page_in_addressbook[counter].zip = input("enter the new zip and press enter")
                    any_more_edit = int(input("1->anymore edit_addressbook\n2->quit"))
                    if any_more_edit == 1:
                        self.edit_addressbook()
                    elif any_more_edit == 2:
                        print("update done successfully")
                        return
                    else:
                        print("not a valid option")
                elif user_selection == 5:
                    self.page_in_addressbook[counter].phone_number = input("enter the new phone_number and press enter")
                    any_more_edit = int(input("1->anymore edit_addressbook\n2->quit"))
                    if any_more_edit == 1:
                        self.edit_addressbook()
                    elif any_more_edit == 2:
                        print("update done successfully")
                        return
                    else:
                        print("not a valid option")
            length_of_addressbook -= 1
            counter += 1

    # function for deleting a particular page/person from the address book
    def delete(self):
        print("deleting the details")
        firstname = input("enter the first_name  of the person")  # getting the necessary details for deleting
        lastname = input("enter the lname of the person")
        length_of_address_book = len(self.page_in_addressbook)
        counter_to_traverse_through_address_book = 0
        while length_of_address_book > 1:  # going through every elements of the list
            # checking whether the first name and last name are matching
            if self.page_in_addressbook[counter_to_traverse_through_address_book].first_name == firstname and \
                    self.page_in_addressbook[counter_to_traverse_through_address_book].last_name == lastname:
                self.page_in_addressbook.remove(self.page_in_addressbook[counter_to_traverse_through_address_book])
                return
            counter_to_traverse_through_address_book += 1
            length_of_address_book -= 1
        print("person not found")

    # method to sort the elements in the address book according to last name
    def sort(self):
        input_for_sort = int(input("select by which category it need to be sorted\n 1->lastname\n2->zipcode"))
        length_of_address_book = len(self.page_in_addressbook)
        counter = length_of_address_book
        while counter > 1:
            if input_for_sort == 1:
                self.page_in_addressbook.sort(key=lambda Person: (Person.last_name,Person.first_name))
            elif input_for_sort == 2:
                self.page_in_addressbook.sort(key=lambda Person: (Person.zip,Person.first_name))
            counter -= 1



number_of_pages = int(input("enter the number of persons to be entered to the address book"))-1
address_book = AddressBook()
for pages in range(number_of_pages):
    address_book.add()
address_book.display_addressbook()
address_book.sort()
address_book.display_addressbook()
address_book.delete()
address_book.display_addressbook()
