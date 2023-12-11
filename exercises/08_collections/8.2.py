# Exercise 8: Collections
# https://gitlab.labranet.jamk.fi/ttc2030/basics-of-programming/-/blob/master/exercises/exercise08.md

"""
8.2.
Shuffle the deck of cards. Implement a shuffle function that shuffles a deck of cards in random order.
Call the shuffle function and print a deck of cards to the console.
"""
# from random import shuffle
import random
from helpers import print_deck

# Generate a deck of 52 cards having 4 suits (clubs, diamonds, hearts and spades)
def generate_card_deck():
    card_deck = []
    suits = ['♣', '♦', '♥','♠']
    # https://en.wikipedia.org/wiki/Playing_cards_in_Unicode
    # ♠ ♥ ♦ ♣ ♤ ♡ ♢ ♧
    for suit in suits:
        for i in range(2,15): # 2-15, cz end-index is not included
            card = i # first card should be 2, we don't have 0 and 1 in cards
            if i == 11: # cards start at 2
                card = 'Jack'
            elif i == 12:
                card = 'Queen'
            elif i == 13:
                card = 'King'
            elif i == 14:
                card = 'Ace'
            card_deck.append(str(f"{suit}{card}"))
    return card_deck

deck = generate_card_deck()
# print("contents of card deck:", deck)


try:
    shuffled_deck = generate_card_deck()
    random.shuffle(shuffled_deck)
    print_deck(shuffled_deck)

except Exception as e:
    print(f"An error occurred: {e}")