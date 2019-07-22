# @author:Muhammed Nisamudheen
# @version:3.7
# @purpose: Determine if it is a Leap Year
from Functional.util import leapyear

try:
    year = int(input("enter a year which is four digit"))
except ValueError as e:
    print("enter a integer", e)
if year > 999 and year < 10000:  # ensuring the number is a four digit number
    print(leapyear(year))
else:
    print("not a valid year")
