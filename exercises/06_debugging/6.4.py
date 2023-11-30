# Exercise 6: Recap and Debugger
# https://gitlab.labranet.jamk.fi/ttc2030/basics-of-programming/-/blob/master/exercises/exercise06.md

"""
6.4.
Five judges are used in the ski jumping. Write a program that asks for rating points for one jump and prints the sum of the style points with the minimum and maximum style points deducted from the sum.

Example output:

  Give points from judge 1: 19
  Give points from judge 2: 20
  Give points from judge 3: 18
  Give points from judge 4: 16
  Give points from judge 5: 20
  Total points are: 57
"""

scores = []
total_points = 0

for i in range (5): # range index starts from 0
  score = int(input(f"Give points from judge {i + 1}: "))
  scores.append(score)

# sort the array so that we have the numbers in order
## methods like insert, remove or sort that only modify the list have no return value printed – they return the default None. 
## This is a design principle for all mutable data structures in Python.
scores.sort()

# Loop over the item excluding the min/max values at start/end of the sorted array
for i in scores[1:4]: # start index included, end index excluded
  total_points+=i

print(f"Total points are: {total_points}")

