# @author:Muhammed Nisamudheen
# @version:3.7
# @purpose:Reading a message and editing it using regex
import re
from datetime import date  # importing the date

initial_string = "Hello <<name>>, We have your full name as <<full name>> in our system.\nyour contact number is 91-xxxxxxxxxx\nPlease,let us know in case of any clarification\nThank you BridgeLabz 01/01/2016."
print(initial_string)  # printing the message
n = input("press yes if you need to change anything")  # asking the user whether he need to change anything
try:
    first_name = input("enter your firstname")  # getting the first name
    last_name = input("enter your lastlame")  # getting the last name
    contact_number = input("enter your contact number")  # getting the contact number
    print(not first_name.isalpha())
    if not first_name.isalpha() or not last_name.isalpha() or not len(
            contact_number) == 10:  # validating the information
        raise ValueError
    initial_string = re.sub("<<name>>", first_name, initial_string)  # replacing using regex
    initial_string = re.sub("<<full name>>", first_name + " " + last_name, initial_string)

    initial_string = re.sub("xxxxxxxxxx", contact_number, initial_string)
    current_day_date_time = date.today()
    current_day_date = current_day_date_time.strftime("%d/%m/%y")  # getting the current date
    string_current_day_date = str(current_day_date)
    initial_string = re.sub("01/01/2016", string_current_day_date, initial_string)  # replacing the current date
    print(initial_string)
except:
    print("something went wrong")
