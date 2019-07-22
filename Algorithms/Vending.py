# @author:Muhammed Nisamudheen
# @version:3.7
# @purpose:Find the Fewest Notes to be returned for Vending Machine

try:
    from Algorithms.util import util
except:
    from util import util

def vendingMachine():

    try:
        amount = int(input("enter the change"))
    except ValueError as e:
        print("enter input value", e)

    count = int()
    coins = (1, 2, 5, 10, 50, 100, 500, 1000)
    length_of_coins = len(coins) - 1

    util.check_coins(amount, count, coins, length_of_coins)

if __name__ == "__main__":
    vendingMachine()
    pass
