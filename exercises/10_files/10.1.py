# Exercise 10: Files
# https://gitlab.labranet.jamk.fi/ttc2030/basics-of-programming/-/blob/master/exercises/exercise10.md

"""
10.1.
Make a program that asks the user for the last names of the people and write the names given by the user to a file (you can decide the termination condition yourself).
Then open the file for reading and print the contents of the file line by line to the console.
Be aware of any exceptions that may be caused by handling the file.
"""

filename = "last_names.txt"
names = []

# def ask_for_input():
#     name = ''
#     while name.lower() != "q":
#         name = input("Give me a name to save to a file. Enter [q] to exit: ")
#         if name.lower() != "q":
#             names.append(name+"\n")

def ask_for_input():
    while True:
        name = input("Give me a name to save to a file. Enter [q] to exit: ")
        
        if name.lower() == "q": break
        
        names.append(name+"\n")
        

def print_lines(array):
    for item in array:
        print(item, end="") 
        # because the list items have \n as part of values, we end up with two line breaks when printing. the end="" removes one line break (the one that the print function adds by default)

def create_file(filename):
    try:
        file = open(filename, "w") # by default the file will be created in the same directory as where script ran
        file.writelines(names)
        file.close()
        print(f"\n{filename} was created and values were added.")
    except Exception as e:
        print(f"ERROR: {filename}", e)

def read_file(filename):
    try:    
        file = open(filename, "r")
        lines = file.readlines()
    except Exception as e:
        print(f"ERROR: Failed to read {filename}", e)
    finally:
        file.close()
        print(f"\nThe contents of {filename} are: ")
        print_lines(lines)

ask_for_input()
create_file(filename)
read_file(filename)
