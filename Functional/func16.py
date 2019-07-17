#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose: prints the wind chil

import sys
from Functional.util import windchill
temperature=int(sys.argv[1])#getting the input from the command prompt
wind_speed=int(sys.argv[2])
print(windchill(temperature,wind_speed))
