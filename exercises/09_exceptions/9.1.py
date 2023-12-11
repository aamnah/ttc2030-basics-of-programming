# Exercise 9: Exception Handling
# https://gitlab.labranet.jamk.fi/ttc2030/basics-of-programming/-/blob/master/exercises/exercise09.md

"""
9.1.
[x] Make a program where you try to change a value in the list that does not exist. 
[x] Start with a list of four elements and then try to change the fifth element. 
[x] Check what kind of exception you get.
[x] Repair the program so that it does not crash.
"""

from bcolors import color

list = [ 'Hanna', 'Jari', 'Ahmed', 'Moosa']

try:
    print(f"Hello {list[4]}")
except IndexError:
    print(f"{color.FAIL}ERROR: Wrong index was used to access list value{color.WARNING}")
except Exception as e:
    print(f"{color.WARNING}ERROR: Something went wrong: {e}{color.WARNING}")
