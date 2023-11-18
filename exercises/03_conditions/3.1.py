# Exercise 3: Conditions
# https://gitlab.labranet.jamk.fi/ttc2030/basics-of-programming/-/blob/master/exercises/exercise03.md

"""
3.1
Make a program that asks the user his/her age.

  - if the age is less than 13 years, print "child"
  - if the age is 13-19 years, print "teen"
  - if it is 20-65 years old, print "adult"
  - otherwise print "senior".
"""

number = int(input("What is your age: "))

if number < 13:
    print("Child")
elif number >= 13 and number <= 19:
    print("Teen")
elif number >= 20 and number <= 65:
    print("Adult")
else:
    print("Senior")