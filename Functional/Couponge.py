# @author:Muhammed Nisamudheen
# @version:3.7
# @purpose:prints the minimum number of steps required for generating a random number
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
import random

unique_set = set()
random_number = random.randint(0, 10)

count = 1
while True:
    # print("inside while")
    random_number = random.randint(0, 10)
    for i in numbers:
        if i == random_number:
            # for j in k:
            # print("inside ol")
            # print("j",j)
            # if j==random_number:
            unique_set.add(random_number)
            numbers.remove(random_number)
            count += 1
            # print(random_number)
            # print(k)
            # print(num)
            # else:
            #     count+=1
        else:
            # print("in else")
            count += 1
    if len(numbers) == 0:
        break
print("minimum steps required go generate random numbers are", count)
