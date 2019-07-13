#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose: prints the wind chil

import sys
t=int(sys.argv[1])#getting the input from the command prompt
v=int(sys.argv[2])
if t<50 and v<120 and v>3:#using formula and calculating necessary
    w=35.74+(0.6215*t)+((0.4275*t)-35.75)*v**0.16
    print(w)
else:
    print("cabnnot be calculated")
