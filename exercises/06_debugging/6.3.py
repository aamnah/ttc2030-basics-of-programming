# Exercise 6: Recap and Debugger
# https://gitlab.labranet.jamk.fi/ttc2030/basics-of-programming/-/blob/master/exercises/exercise06.md

"""
6.3.
Make a program that asks for the names of the students until the user provides a blank input. The program then tells you how many names were given and displays them in a single line separated by commas.
NOTE: You may need to peek ahead to 'Collections' lesson and check out how to use list to make this work.

Example output:

  Enter student name:Minna
  Enter student name:Matti
  Enter student name:Kirsi
  Enter student name:Arto
  Enter student name:
  Student count: 4
  Minna, Matti, Kirsi, Arto
"""
students = []

while True:
  name = input("Enter student name: ")

  if name == "": break
  
  students.append(name)

output = ', '.join(students)

print(f"Student count: {len(students)}")
print(output)