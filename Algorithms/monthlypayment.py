#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:reads in three command-line arguments P, Y, and R and calculates the monthly payments you would have to make over Y years to pay off a P principal loan amount at R per cent interest compounded monthly
from Algorithms.util import util
import sys
principle_amount=int(sys.argv[1])#getting the parameters from the command line
year=int(sys.argv[2])#getting the parameters from the command line
rate_of_interest=int(sys.argv[3])#getting the parameters from the command line
amount=util.monthlyPayment(principle_amount,year,year)#calculating and finding the amount
print("your payment amount is ",amount)