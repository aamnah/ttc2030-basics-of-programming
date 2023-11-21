# Exercise 2: Variables
# https://gitlab.labranet.jamk.fi/ttc2030/basics-of-programming/-/blob/master/exercises/exercise02.md

"""
2.2 
[x] Create a program that asks two integer numbers from the user and prints result of their their:
    [x] Sum
    [x] Subtraction
    [x] Multiplication
    [x] Division
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