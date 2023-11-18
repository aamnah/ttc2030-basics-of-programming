# Exercise 3: Conditions
# https://gitlab.labranet.jamk.fi/ttc2030/basics-of-programming/-/blob/master/exercises/exercise03.md

"""
3.2.
Make a program that asks the user for 3 integers and prints the largest of them.

Example output:

  Input integer: 2
  Input another integer: 3
  One more: 1
  Max value: 3
"""

integers = []

integers.append(int(input('Give me an integer: ')))
integers.append(int(input('Give me another integer: ')))
integers.append(int(input('Give me one more integer: ')))


print ('Max value: ', max(integers))