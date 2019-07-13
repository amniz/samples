#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:This program takes a command-line argument N and prints a table of the powers of 2 that are less than or equal to 2^N.
# Print the year is a Leap Year or not.
import sys
n=int(sys.argv[1])#getting the command line arguments
t=2**n
from util import twopow
twopow(n,t)#checking for leap year or not
