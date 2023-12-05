# Exercise 8: Collections
# https://gitlab.labranet.jamk.fi/ttc2030/basics-of-programming/-/blob/master/exercises/exercise08.md

"""
8.1.
Implement a program that stores the playing cards in a standard 52-card deck. The suits are: clubs, diamonds, hearts and spades; card values range from 1-13. Use the collection of your choice to store the cards and print a deck of cards to the console.
"""

"""
NOTES:
    - There can't be two of the same card
    - There will be 52 cards, we have to print the entire deck to the console

use a loop to generate the suits? (clubs, diamonds, hearts and spades)
"""

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

def print_deck(deck):
    new_deck = deck
    pointer = 13
    # make it look pretty
    # Add a line break after every 13 items (one suit has 13 cards)
    # basically print every suit on it's own line
    for i in range (1,5): # 5 not included, will run four times
        new_deck.insert(pointer, '\n')
        pointer += (13 + 1) # 13, 27, 41, 55 (the list will be displaced by 1 because of the new item we added)

    for index, i in enumerate(new_deck):
        if i != "\n":
            print(i, end = " ")
        else: print(i)


print_deck(deck)
