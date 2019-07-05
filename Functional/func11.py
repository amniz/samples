#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose: program Distance.java that takes two integer command-line arguments x           and y and prints the Euclidean distance from the point (x, y) to the origin (0, 0). The                  formulae to calculate distance = sqrt(x*x + y*y).
import sys
import math

n=int(sys.argv[1])
n1=int(sys.argv[2])

distance=math.sqrt(n**n+n1**n1)
print(distance)
