# Exercise 9: Exception Handling
# https://gitlab.labranet.jamk.fi/ttc2030/basics-of-programming/-/blob/master/exercises/exercise09.md

"""
9.3.
Check out the TypeError exception in this document:
https://docs.python.org/3/library/exceptions.html
[x] Implement the function isthiszero(num). The function accepts one parameter. 
    [x] The function returns true if the parameter value is zero. 
    [x] The function returns false if the parameter is a number but not zero. 
    [x] The function raises the TypeError exception if the parameter is not a number. 
[x] Try calling functions with different values from the program. For the calling program, use try-except. What do you notice? 
[x] Answers to the beginning of the task as comments.
"""

"""
I noticed that i can raise custom exceptions myself. If i raise an exception inside a function, 
i will have access to it in the calling try/except block and can show it to the user
"""

from bcolors import color

def isthiszero(num):
    if num == 0:
        return True
    if type(num) is int and num != 0:
        return False
    if type(num) is not int:
        raise TypeError(f"{color.WARNING}This value is a number but not zero{color.ENDC}")

try:
    isthiszero(1)
    isthiszero(0)
    isthiszero('yo')
except Exception as e:
    print(f"ERROR: {e}")