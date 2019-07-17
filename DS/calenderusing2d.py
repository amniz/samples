# @author:Muhammed Nisamudheen
# @version:3.7
# @purpose: prints the claender of a given date using a 2d array.
from DS.util import util
import sys

month = int(sys.argv[1])  # getting the data using commandline
year = int(sys.argv[2])
start_day_of_mnth = util.daysofWeek(month, year)
start_day_of_month = int(start_day_of_mnth)
empty_space = start_day_of_month + 9   # adding space for the first 1-10 digits
days = [x for x in range(1, util.monthDay(month, year))]
print("     python cal", month, " ", year)
print("    S   M  T   W  Th   F   S")
calender = []
value = 42  # 6*7 columns present in calender
counter = 0
while value > 0:
    temp_array = []  # temparory array to add the elements and later to append to the calender for ensuring 2d array
    row_counter = 0  # counter to break after each 6th element

    while row_counter <= 6:
        while start_day_of_month > 0:  # adding the empty space
            temp_array.append(" ")
            row_counter += 1
            value -= 1
            start_day_of_month -= 1
        try:  # appending the days in number
            temp_array.append(days[counter])
            counter += 1
            row_counter += 1
            value -= 1
        except:  # when list index exception is thrown adding space
            temp_array.append(" ")
            counter += 1
            row_counter += 1
            value -= 1
    calender.append(temp_array)

for dates in calender:

    row_counter = 0   # counter to break after each 6th element
    while row_counter <= 6:  # printing each row in the calender
        if empty_space > 0:
            print("  ", dates[row_counter], end="")
            row_counter += 1
            empty_space -= 1
        else:
            print(" ", dates[row_counter], end="")
            row_counter += 1
    print()
