# @author:Muhammed Nisamudheen
# @version:3.7
# @purpose:Reading a file from json
import json
read_json=json.load(open("inventory.json","r"))  # reading from json
for dictionary_key in read_json.keys():  # getting every key values in the dictionary
    length_of_dictionary_key=len(read_json[dictionary_key])  # getting the length of particular keys value in dictionary
    counter = 0  # initializing a counter to print each element in the list of dictionary read_json
    while counter<length_of_dictionary_key:  # traversing through each of the element of the first 'key' in dictionary
        print(read_json[dictionary_key][counter])  # printing the respective values of the key
        counter+=1  # incrementing the counter



