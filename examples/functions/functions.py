# Functions
# Material - https://gitlab.labranet.jamk.fi/ttc2030/basics-of-programming/-/blob/master/materials/10-functions.md
# Examples - https://gitlab.labranet.jamk.fi/ttc2030/basics-of-programming/-/blob/master/examples/10-functions/functions.py


# function / method / procedure

'''
Function:
A piece of a program code called by its name. Variables can be send to the function as parameters and it can return data

Method:
Function inside a class is called a method

Procedure:
a function that does not return anything
'''

random_number = 33


def functionName(optionalParams):
  print('yo, this is a function')

functionName('assa')


def print_info():
  print('info')

print_info()

# function that returns a value
def print_and_return_number():
  print('Info - returning 123')
  return 123

# you can use the returned value from calling the function as a param value for another function
print('print_and_return_number returned: ', print_and_return_number())

# assign the returned value to a variable
number = print_and_return_number()
print('print_and_return_number returned: ', number)


# we can use function calls in our condition statements
if print_and_return_number() == 123:
  print('print_and_return_number returned: ', number)


# Functions can access global variables
def lets_access_global_vars():
  print(random_number, 'is a global variable')

lets_access_global_vars()