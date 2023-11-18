# Exercise 3: Conditions
# https://gitlab.labranet.jamk.fi/ttc2030/basics-of-programming/-/blob/master/exercises/exercise03.md

"""
3.4.
Make a program that asks the user for five numbers. Calculate sum of entered numbers, but include only the numbers that are greater than zero.
Print the amount to the console. Try your program with the following values: 1,2,3,4,5 and -2,0,2,4,6.

Example output:
  Input number: -2
  Input number: 0
  Input number: 2
  Input number: 4
  Input number: 6
  Sum is 12
"""

numbers = []
total = 0

# Ask for five numbers, and add them to the numbers array
for x in range(0,5): # stop value (here 5) is not included when the range is executed
  numbers.append(int(input('Input number: ')))

# Add all the values in the numbers array to the total variable
for x in numbers:
  if x > 0:
    total += x

# Print total
print('Sum is:', total)