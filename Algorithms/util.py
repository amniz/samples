# @author:Muhammed Nisamudheen
# @version:3.7


import sys


class util:
    ####################################################################################################################
    # @purpose:Anagram Detection
    @staticmethod
    def anagram(string1, string2):

        sort1 = sorted(string1)  # sorting both of the strings using sorted method
        sort2 = sorted(string2)
        if sort1 == sort2:
            print("entered string is anagram")
        else:
            print("entered string is not anagram")

    ######################################################################################################################
    # @purpose: Prime numbers in the range of 0 - 1000
    @staticmethod
    def isPrime():
        list_of_prime = []
        try:
            number = int(input(
                "enter the number number till prime number is to be generated"))  # asking the user to enter a particular number
        except ValueError as e:
            print("please do enter an integer", e)
        if number > 0 and number <= 1000:  # checking the number is in the range of 0-1000
            for each_number in range(2, number + 1):

                if each_number == 2:  # appending the number 2
                    list_of_prime.append(each_number)
                else:
                    second_iterartor_variable = 2  # setting an iterator variable to traverse till each_number
                    while (second_iterartor_variable <= each_number):  # traversing
                        if each_number % second_iterartor_variable == 0:  # checking whether any divisors are there for the number
                            break

                        else:
                            second_iterartor_variable += 1

                    if second_iterartor_variable == each_number:
                        list_of_prime.append(each_number)  # appending the number
        return list_of_prime

    #######################################################################################################################
    def rev(l):  # reversing and checking for palindrome
        set1 = set()
        for i in l:

            j = i
            val = 0
            while j > 0:
                rem = j % 10

                val = val * 10 + rem

                j = j // 10

            set1.add(val)
            return set1

    def rev1(l):  # reversing and checking for anagram
        set2 = set()
        for i in l:
            j = i
            val = 0
            while j > 0:
                rem = j % 10

                val = val * 10 + rem

                j = j // 10

            if (val == i):
                if (i > 9):
                    set2.add(val)
            return set2

    #################################################################################################################################
    # method to do binary search on a particular item
    def BinarySearch(array, last, first, key):
        if last >= first:
            mid = int((first + last) / 2)
            if array[mid] == key:
                return array[mid]
            elif array[mid] > key:
                util.BinarySearch(array, mid - 1, first, key)
            else:
                util.BinarySearch(array, last, mid + 1, key)
        else:
            return -1

    #################################################################################################################################
    # @purpose:Insertion Sort,given a list of values returns the sorted values
    @staticmethod
    def Insertionsort(array):
        for per_array_element in range(1, len(array)):
            key = array[per_array_element]
            previous_element = per_array_element - 1
            while previous_element > -1 and array[previous_element] > key:
                array[previous_element + 1] = array[previous_element]
                previous_element -= 1
            array[previous_element + 1] = key
        return array

    ###################################################################################################################################
    # @purpose:BubbleSort,given a list of values returns the sorted values
    @staticmethod
    def BubbleSort(values):
        for i in range(1, len(values)):
            for j in range(0, len(values) - i):
                if values[j] > values[j + 1]:
                    temperory_variable = values[j]
                    values[j] = values[j + 1]
                    values[j + 1] = temperory_variable
        return values

    #############################################################################################################################
    def daysofWeek(m, d, y):

        # y0 = int()
        # x = int()
        # m0 = int()
        # d0 = int()
        y0 = y - (14 - m) / 12
        x = y0 + y0 / 4 - y0 / 100 + y0 / 400;
        m0 = m + 12 * ((14 - m) / 12) - 2;
        d0 = (d + x + 31 * m0 / 12) % 7;
        d0 = int(d0)
        d0;
        if (d0 == 0):  # checking for the corresponding day
            return "sunday"
        elif d0 == 1:
            return "monday"
        elif d0 == 2:
            return "tuesday"
        elif d0 == 3:
            return "wednwsday"
        elif d0 == 4:
            return "thursday"
        elif d0 == 5:
            return "friday"
        else:
            return "saturday"

    ##########################################################################
    def monthlyPayment(principle_amount, year, rate_of_interest):
        n = 12 * year
        r = rate_of_interest / (12 * 100)
        payable_amount = (principle_amount * r) / (1 - (1 + r) ** (-n))
        return payable_amount

    ###############################################################################
    # method to convert given decimal number to binary
    def tobinary(number):
        store_initial_converted_data = str()
        while number >= 1:  # dividing the number by 2 and getting the reminder and storing it
            store_initial_converted_data += str(int(number % 2))
            number /= 2
        length_initial_converted_data = len(store_initial_converted_data)
        while length_initial_converted_data < 32:  # adding zeros to the rest of the vacent postions
            store_initial_converted_data += "0"
            length_initial_converted_data += 1
        store_final_32bit_data = str()
        while length_initial_converted_data > 0:  # appending zeros and the converted data
            length_initial_converted_data -= 1
            store_final_32bit_data += store_initial_converted_data[length_initial_converted_data]
        return store_final_32bit_data
        ######################################################################

    def check_coins(amount, count, coins, length_of_coins):
        amount = amount
        count = count
        length_of_coins = length_of_coins
        if amount == 0:
            print("total number of coins", count)
            count
        else:
            if amount / coins[length_of_coins] >= 1:  # dividing the amount and getting the necessary result
                print(int(amount / coins[length_of_coins]), "coins of", coins[length_of_coins], "rupees coin")
                count += int(amount / coins[length_of_coins])  # incrementing the coin count
                amount %= coins[length_of_coins]  # reminder will be the remaining amount
                util.check_coins(amount, count, coins, length_of_coins)  # recursive function call until the number is not further divisible
            else:
                length_of_coins -= 1  # changing the coin
                util.check_coins(amount, count, coins, length_of_coins)  # recursive call with new coin
