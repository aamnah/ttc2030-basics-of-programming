# Exercise 4: Loops
# https://gitlab.labranet.jamk.fi/ttc2030/basics-of-programming/-/blob/master/exercises/exercise04.md

"""4.1.
Make a program that asks the user for the first and last name. Print the first letter of the user's first name as many times as there are letters in the first name. Then print the user's last name in reverse order.
For example, if the user gives the first name 'Cherry' and the surname 'Kernell' the output would be:

Example output:

  Enter first name: Cherry
  Enter last name: Kernell
  CCCCCC llenreK
"""

first_name = input('Enter first name: ')
last_name = input('Enter last name: ')

def repeat_first_letter(str):
    """
  repeat_first_letter
    ---
    Repeats the first first letter of the provided string 
    as many times as there are letters in the string
    
    Parameters
    ---
    str : string
      A string passed to the function
    
    Returns
    ---
    str
      A string that repeats the first letter from the provided string as many times as it's length
    """
    iteration_count = len(str)
    first_letter = str[0]
    new_word = ''

    while iteration_count > 0:
        new_word += first_letter
        iteration_count -= 1
    
    return new_word

def reverse_string(str):
    """
    Takes a string and returns it reversed
    """
    # The reversed() function returns a reversed iterator object.
    # reversed_str = ''.join(reversed(str))
    reversed_str = ''

    for i in str:
        reversed_str = i + reversed_str
    return reversed_str


# RUN
print(repeat_first_letter(first_name), reverse_string(last_name))