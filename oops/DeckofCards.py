# @author:Muhammed Nisamudheen
# @version:3.7
# @purpose:Reading a message and editing it using regex
import random  # importing random function
import itertools  # importing itertools for cartesian product


# function to produce deck of cards
def deckofcard():
    suit = ["Clubs", "Diamonds", "Hearts", "Spades"]  # suit of cards
    Rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]  # rank of cards
    # using product method to produce the cartesian product of the cards
    cartesian_product_of_list_suit_rank = itertools.product(suit,Rank)

    list_of_cartesian_product_list_suit_rank = list(
        cartesian_product_of_list_suit_rank)  # converting iterttol objects to list
    random.shuffle(list_of_cartesian_product_list_suit_rank)  # shuffling the cards

    # making two dimensional array necessary for printing

    total_cards_counter = 0  # counter  to ensure loop run 52 times
    counter_for_13_cards = 1  # counter to ensure a break on every 13th card
    # k = 1
    list_for_adding_cards = []  # list for adding the pair on each iteration
    list_for_adding_all_pair_cards = []  # list for adding the 4 pairs of cards
    # print("player", k, "card->",end="")
    while total_cards_counter < 52:  # printing the cards

        if counter_for_13_cards != 13:  # breaking when the counter reaches 13
            # appending every element to a list
            list_for_adding_cards.append(list_of_cartesian_product_list_suit_rank[total_cards_counter])

            total_cards_counter += 1  # incrementing the total_cards_counter
            counter_for_13_cards += 1 # incrementing the counter which ensures the change of list at 13
        else:
            counter_for_13_cards = 0  # reassigning the counter_for_13_cards to break again at 13
            list_for_adding_cards.append(list_of_cartesian_product_list_suit_rank[total_cards_counter])
            list_for_adding_all_pair_cards.append(list_for_adding_cards)
            list_for_adding_cards = []


    return list_for_adding_all_pair_cards


cards = deckofcard()
for counter in range(0, 4):
    print("cards of player", counter + 1, "->", cards[counter])
