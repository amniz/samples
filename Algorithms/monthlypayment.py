#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:reads in three command-line arguments P, Y, and R and calculates the monthly payments you would have to make over Y years to pay off a P principal loan amount at R per cent interest compounded monthly
from Algorithms.util import util
import sys
P=int(sys.argv[1])#getting the parameters from the command line
Y=int(sys.argv[2])#getting the parameters from the command line
R=int(sys.argv[3])#getting the parameters from the command line
util.monthlyPayment(P,Y,R)#calculating and finding the amount
