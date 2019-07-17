#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:This program takes a command-line argument N and prints a table of the powers of 2 that are less than or equal to 2^N.
# Print the year is a Leap Year or not.
from Functional.util import two_power
import sys
number=int(sys.argv[1])#getting the command line arguments
times=2**number

two_power(number,times)#checking for leap year or not
