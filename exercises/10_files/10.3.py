# Exercise 10: Files
# https://gitlab.labranet.jamk.fi/ttc2030/basics-of-programming/-/blob/master/exercises/exercise10.md

"""
10.3.
[x] Make a program that asks the user for numbers (either an integer or a floating point number) and 
[x] save the integers in a different file than the floating point numbers.
[x] The application should be terminated if the user does not enter an integer or a floating point number.
[x] Use a text editor to check the contents of the files.
"""

filename_int = 'integers.txt'
filename_flt = 'floats.txt'

def is_integer(x):
    try:
        isinstance(int(x), int)
        return True
    except ValueError:
        return False

def write_number_to_file(x):
    try:
        file_int = open(filename_int, "a") # a is for append mode
        file_flt = open(filename_flt, "a")

        if (is_integer(x)):
            file_int.write(x+"\n")
        else:
            file_flt.write(x+"\n")

        file_int.close()
        file_flt.close()
    except Exception as e:
        print(f"ERROR: {e}")


while True:
    number = input("Gimme an integer or floating point number: ")
    
    if number == "": break

    write_number_to_file(number)
    
