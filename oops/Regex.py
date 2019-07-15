#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:Reading a message and editing it using regex
import re
from datetime import date#importing the date
s="Hello <<name>>, We have your full name as <<full name>> in our system.\nyour contact number is 91-xxxxxxxxxx\nPlease,let us know in case of any clarification\nThank you BridgeLabz 01/01/2016."
print(s)#printing the message
n=input("press yes if you need to change anything")#asking the user whether he need to change anything
try:
    fname=input("enter your firstname")#getting the first name
    lname=input("enter your lastlame")#getting the last name
    cn = input("enter your contact number")#getting the contact number
    print(not fname.isalpha())
    if not fname.isalpha() or not lname.isalpha() or not len(cn)==10:#validating the information
        raise ValueError
    s=re.sub("<<name>>",fname,s)#replacing using regex
    s=re.sub("<<full name>>",fname+" "+lname,s)


    s=re.sub("91-xxxxxxxxxx",cn,s)
    h=date.today()
    tdy=h.strftime("%d/%m/%y")#getting the current date
    tod=str(tdy)
    s=re.sub("01/01/2016",tod,s)#replacing the current date
    print(s)
except:
    print("something went wrong")