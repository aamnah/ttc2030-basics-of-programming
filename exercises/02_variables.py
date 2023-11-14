# Exercises 2: Variables
# https://gitlab.labranet.jamk.fi/ttc2030/basics-of-programming/-/blob/master/exercises/exercise02.md

"""
2.1.
Create a program that declares a variable that stores persons height in full centimeters. Print the value of the variable into the console.
"""
height_in_cm = 161

print(height_in_cm)



"""
2.2 
Create a program that asks two integer numbers from the user and prints result of their their:

Sum
Subtraction
Multiplication
Division
"""
def maths():
    """takes two numbers and does a bunch of math operations on them, prints results

    Parameters
    ----------
    number_a : int
        a number that will be added, subtracted, multiplied and divided by another number
    number_b : int
        a number that will be added, subtracted, multiplied and divided from another number

    Returns
    -------
    int
    """
    # input is a string, cast it as an int
    number_a = int(input('Enter a number (integer): '))
    number_b = int(input('Enter another number (integer): '))

    sum = number_a + number_b
    subtract = number_a - number_b
    multiply = number_a * number_b
    division = number_a / number_b

    output = """
Sum: {}
Subtraction: {}
Multiplication: {}
Division: {}
""".format(sum, subtract, multiply, division)  

    print(output)

maths()



"""
2.3.
Declare a variable which is used to store bank account balance in euro (start balance of 2000 €). Print current balance into the console. Ask from user how many euro will be added to the balance. Then ask how many cents are added to the balance. Print the balance after user requested changes are made.
"""

bank_balance_eur = 2000

print('Bank account balance: {} €'.format(bank_balance_eur))

add_euro = int(input('How many euro will be added to the balance? '))
add_cent = int(input('How many cents will be added to the balance? '))

bank_balance_eur += add_euro
bank_balance_eur += add_cent / 100

print('Bank account balance: {} €'.format(bank_balance_eur))

print()