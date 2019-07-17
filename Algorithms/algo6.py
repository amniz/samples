#@author:Muhammed Nisamudheen
#@version:3.7
#@purpose:> Read in a list of words from File. Then prompt the user to enter a word to
#search the list. The program reports if the search word is found in the list.
from Algorithms.util import util#importing from util
try:
    with open("abc.txt","r") as file:#reading the file
        file_input=file.readlines()
except FileNotFoundError as e:
    print("file not found",e)
    # word="hai hello how are you"
    # with open("abc.txt","w") as file:#creating the file if it is not created
    #     write_to_file=file.write(word)
    # with open("abc.txt","r") as file:#reading the file
    #     d=file.readlines()

add_file_words=[]
for words in file_input:
    line=words.split()
    add_file_words.extend(line)#splitting ti each word
util.Insertionsort(add_file_words)#sorting the words using insertion sort
#print(add_file_words)
s=input("enter the word to be searched")
result=util.BinarySearch(add_file_words,len(add_file_words),0,s)#searching the word using binary search
if result!=1:
    print("  found")
else:
    print("word not found")
