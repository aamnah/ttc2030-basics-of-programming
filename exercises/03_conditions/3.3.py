# Exercise 3: Conditions
# https://gitlab.labranet.jamk.fi/ttc2030/basics-of-programming/-/blob/master/exercises/exercise03.md

"""
3.3
Make a program that gives the student a grade according to the table below.
Ask for a points on the console and print the grade.

Example output:

  Insert your points: 1
  Grade: 0

  Insert your points: 7
  Grade: 3
"""

points = int(input('Insert your points: '))
grade = 0

if 0 <= points <= 1:
    grade = 0
elif 2 <= points <= 3:
    grade = 1
elif 4 <= points <= 5:
    grade = 2
elif 6 <= points <= 7:
    grade = 3
elif 8 <= points <= 9:
    grade = 4
elif 10 <= points:
    grade = 5

print('Grade: ', grade)