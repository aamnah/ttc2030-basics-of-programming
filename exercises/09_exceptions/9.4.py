# Exercise 9: Exception Handling
# https://gitlab.labranet.jamk.fi/ttc2030/basics-of-programming/-/blob/master/exercises/exercise09.md

"""
9.4.
[x] Make a collection with 5 strings.
[x] Ask the user index where in the table the user wants to modify existing text.
[x] Ask the user for the new text and put it in a table in the index provided by the user.
[x] Print the contents of the table.
[x] Repair the program so that it does not crash if the user enters an index that is outside the table.
[x] Tell the user if the index is not valid and ask to enter it again.
"""
from bcolors import color

feelings = ['satisfied', 'delighted', 'awesome', 'happy', 'amazed']


def ask_for_input():
    global index, value
    index = int(input("\nWhat index value would you like to edit? Give [index]: "))
    value = input("What value would you like to add? ")

def print_list(x):
    print("Here are the contents of list: ")

    for key, value in enumerate(x):
        print(f"{key}: {value}")

def update_list(list, index, value):
    if not (0 <= index <= (len(list) - 1)):
        raise IndexError(f"The index you provided is not correct. Index should be between 0-{(len(list) - 1)}.\nPlease provide the index again.")
    else: 
        list[index] = value
        print("\nValue successfully added.")
        print_list(list)

try:
    print_list(feelings)
    ask_for_input()
    update_list(feelings, index, value)
except IndexError as e:
    print(f"{color.WARNING}ERROR: {e}{color.ENDC}")
    ask_for_input()
    update_list(feelings, index, value)
except Exception as e:
    print(f"{color.WARNING}ERROR: {e}{color.ENDC}")
