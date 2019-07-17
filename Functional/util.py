import random
import math


# function to generate random number and gives the output of number of heads and tails
def random_number_generator(toss_times):
    tail = 0
    head = 0
    while toss_times > 0:  # tossing n number of times
        rand = random.random()
        # print(rand)
        if rand >= 0.5:  # checking for heads
            head += 1
            toss_times -= 1
        else:  # checking for tails
            tail += 1
            toss_times -= 1
    return head, tail


# function to check whether a given year is leap year or not
def leapyear(year):
    if year % 400 == 0:  # checking whether divisible by 400
        return "is a leap year"
    elif year % 100 == 0:  # checking whether divisible by 100
        return "is not a leap year"
    elif year % 4 == 0:  # checking whether divisible by 4
        return "is a leap year"
    else:
        return "is not a leap year"


# function to print the powers of to and gives the output whether it is a leap year or not
def two_power(number, times):
    if number > 31 or number < 0:  # ensuring the number is between 0 and 31
        print("over flow")
    else:
        while times > 0:
            print(times, " ", end="")
            print(leapyear(times))  # passing parameter to leap year to check whether the given year is leap year or not
            print(end="\n")
            times = int(times / 2)


# function to print the nth harmonic number
def harmonic_number(number):
    times = 1
    sum = 0
    while times <= number:  # generating and printing the harmonic number
        sum = 1 / times

        print("1/", times, "=", 1 / times)
        times += 1
    return sum


# gambler function plays the game until gambler wins or lose the stake
def gambler(stake, goal, time):
    count = int()
    win = 0
    loss = 0
    while time > 0:  # playing n number of time

        temperory_stake = stake
        while temperory_stake > 0 and temperory_stake < goal:  # playing a specific game untill goal reached or stakes runs out
            # print(time,"inside while")
            count += 1
            random_number = random.random()  # generating random numbers
            # print(random_number)
            if random_number > 0.5:  # generating win
                temperory_stake += 1
                win += 1
                # print("won")
            else:  # generating loss
                temperory_stake -= 1
                loss += 1
                # print("loss")

        print(time, "time-> win percentage is ", win / count)  # calculating win
        print(time, "time-> loss percentage is ", loss / count)  # calculating loss
        time -= 1


# creates random coupon which is a mix of alpha numeric character
def coupon(number_of_coupons):
    coupon_string = "0qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"  # for generating random numbers
    # print(s.length)
    # max=1000
    # print(len(s))

    final_set = set()  # avoiding duplicate elements
    while number_of_coupons > 0:  # generating random numbers n number of times
        coupon = ""
        # print("n",n)
        max_value = 10000
        while max_value > 0:  # generating random number
            rand = int(random.uniform(1, 62))  # generating a random number between 1 and 62
            # print(rand)
            coupon += coupon_string[rand]  # appending the character to the string
            max_value = int(max_value / rand)
            # print(coupon)
        final_set.add(coupon)  # adding the coupon
        number_of_coupons -= 1
    return final_set


# function which return a  boolean 2D array
def Boolean_array(row, column):  # function to generate boolean array
    array = []
    while row > 0:  # entering the elementts to the row
        temparory_row = []
        temparory_column = column
        while temparory_column > 0:  # entering the elements to the column
            element = bool(input("enter the element if it is a true value else press enter"))
            temparory_row.append(element)
            temparory_column -= 1
        array.append(list(temparory_row))  # adding the particular element
        row -= 1
    print(array)


# function which returns the array of Integers
def Integer_array(row, col):  # function to generate integer array
    array = []
    while row > 0:  # entering the elementts to the row
        temparory_row = []
        temparory_column = col
        while temparory_column > 0:  # entering the elements to the column
            element = int(input("enter the element"))
            temparory_row.append(element)
            temparory_column -= 1
        array.append(list(temparory_row))
        row -= 1
    print(array)


# function which returns the array of float
def Float_array(row, col):  # function to generate double array
    array = []
    while row > 0:  # entering the elementts to the row
        temparory_row = []
        temparory_column = col
        while temparory_column > 0:  # entering the elements to the column
            element = float(input("enter the element"))
            temparory_row.append(element)
            temparory_column -= 1
        array.append(list(temparory_row))  # adding the particular element
        row -= 1
    print(array)


# function to check for distinct triplets which sum to zero
def check_triplets(number_of_elements):
    element_list = []
    final_list_of_triplets = []
    while number_of_elements > 0:
        element_list.append(int(input("enter the element")))
        number_of_elements -= 1
    for i in element_list:  # checking for the triplets which sum to zero
        for j in element_list:
            for k in element_list:
                if i + j + k == 0:  # if triplets sum is zero then adding the elements
                    count = 0
                    list_triplets = []
                    list_triplets.append(i)
                    list_triplets.append(j)
                    list_triplets.append(k)
                    temparory_tuple = tuple(list_triplets)
                    final_list_of_triplets.insert(count, temparory_tuple)
                    # print(i,j,k)
                else:
                    continue
    set_of_triplets = set(final_list_of_triplets)  # avoiding the duplicate elements
    return set_of_triplets


# function which calculate the distance between two points in euclidean plane
def distance_calculation(first_point, second_point):
    distance = math.sqrt(first_point ** first_point + second_point ** second_point)  # calculating using the formula
    return distance


# checking for the winner of the tic tac toe game
def check_winner(tic_tac_toe, n):
    human = 0
    computer = 0
    for row in range(3):
        for column in range(1):  # checking through the rows human
            if tic_tac_toe[row][column] == 'x' and tic_tac_toe[row][column + 1] == 'x' and tic_tac_toe[row][
                column + 2] == 'x':
                human += 1
    for row in range(3):  # checking through the row for computer
        for column in range(1):
            if tic_tac_toe[row][column] == 'o' and tic_tac_toe[row][column + 1] == 'o' and tic_tac_toe[row][
                column + 2] == 'o':
                computer += 1
    for column in range(1):  # checking through the column for human
        for row in range(3):
            if tic_tac_toe[column][row] == 'x' and tic_tac_toe[column + 1][row] == 'x' and tic_tac_toe[column + 2][
                row] == 'x':
                human += 1
    for column in range(1):  # checking through the column for computer
        for row in range(3):
            if tic_tac_toe[column][row] == 'o' and tic_tac_toe[column + 1][row] == 'o' and tic_tac_toe[column + 2][
                row] == 'o':
                computer += 1
    if tic_tac_toe[0][0] == 'x' and tic_tac_toe[1][1] == 'x' and tic_tac_toe[2][2] == 'x' or tic_tac_toe[0][
        2] == 'x' and tic_tac_toe[1][1] == 'x' and tic_tac_toe[2][1] == 'x':
        human += 1  # checking through the diagonal for human
    if tic_tac_toe[0][0] == 'o' and tic_tac_toe[1][1] == 'o' and tic_tac_toe[2][2] == 'o' or tic_tac_toe[0][
        2] == 'o' and tic_tac_toe[1][1] == 'o' and tic_tac_toe[2][1] == 'o':
        computer += 1  # checking through the diagonal for computer
    if computer or human == 1 and n < 3:  # checking for the winner
        if human > computer:
            print("human wins")
        elif computer > human:
            print("computer wins")
        else:
            print("match draw")


# displaying the tic tac toe game
def display_tic_tac_toe(tic_tac_toe):  # displaying the elements
    for row in range(0, len(tic_tac_toe)):
        column = 0
        while column < 3:
            print(tic_tac_toe[row][column], "|", end='')
            column += 1
        print()


# calculates the wind chill using the formula
def windchill(temperature, wind_speed):
    if temperature < 50 and wind_speed < 120 and wind_speed > 3:  # using formula and calculating necessary
        wind_chill = 35.74 + (0.6215 * temperature) + ((0.4275 * temperature) - 35.75) * wind_speed ** 0.16
        return wind_chill
    else:
        return "cannot be calculated"
