# Exercise 4: Loops
# https://gitlab.labranet.jamk.fi/ttc2030/basics-of-programming/-/blob/master/exercises/exercise04.md

"""
4.2.
Make a function lottery(), which draws the 7 random numbers of the lottery line in range 1-40. Verify that one lottery line does not include same number multiple times. Ask user how many lottery number sets to generate and print them to the console.
To generate random numbers, use Pythons random module, see more: https://www.w3schools.com/python/gloss_python_random_number.asp

Example output:

  How many sets of lottery numbers to generate: 3
  2,7,12,19,27,33,38
  3,8,13,29,28,35,39
  4,9,14,21,29,37,40
"""

import random


def generate_unique_random_numbers(count):
    """
    Generate a row of unique random numbers

    Parameters
    ----------
    count : int
      The amount of numbers to generate

    Returns 
    ----
    str
      row of comma separated unique numbers
    """
    nums = []

    # Generate 7 unique random numbers 
    while count > 0:
        random_number = random.randrange(1,40)
        if random_number in nums:
          # if random number is already in the array, generate a new one
            random_number = random.randrange(1,40)
        else:
            # else, add it to the array
            nums.append(random_number)
            count -= 1

    # Print the numbers in the requested format
    print(','.join(str(e) for e in nums))

    return nums


def lottery():
    """
    Generate sets of unique random numbers

    Parameters
    ----------
    number_of_sets : int
      The number of sets to generate

    Returns 
    ----
    str
      rows of comma separated unique numbers
    """

    number_of_sets = int(input('How many sets of lottery numbers to generate: '))

    while number_of_sets > 0:
        generate_unique_random_numbers(7)
        number_of_sets -= 1



# RUN 
lottery()


