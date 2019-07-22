#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose: takes a date as input and prints the day of the week that date falls on.

import sys
try:
    from Algorithms.util import util
except:
    from util import util

month=int(sys.argv[1])#getting the parametrs from command line
day=int(sys.argv[2])#getting the parametrs from command line
year=int(sys.argv[3])#getting the parametrs from command line

print(util.daysofWeek(month,day,year))

    
