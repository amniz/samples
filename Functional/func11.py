#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose: program Distance.java that takes two integer command-line arguments x           and y and prints the Euclidean distance from the point (x, y) to the origin (0, 0). The                  formulae to calculate distance = sqrt(x*x + y*y).
import sys
import math
from Functional.util import dist
n=int(sys.argv[1])#getting the input through command line
n1=int(sys.argv[2])

distance=dist(n,n1)
print(distance)
