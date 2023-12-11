# Exercise 10: Files
# https://gitlab.labranet.jamk.fi/ttc2030/basics-of-programming/-/blob/master/exercises/exercise10.md

"""
10.2.
[x] Using an editor (such as Notepad), create a text file 'names.txt' to which you add at least ten women's and ten men's first names.
[x] Make a program that reads the names from the above text file and 
[x] tells you how many names can be found and 
[x] how many times each name occurs. 
[x] Sort the names alphabetically before printing.
[x] Also note any other exceptions that may be caused by handling the file.
"""


filename = "names.txt"

def print_dict(dict):
    for key, value in dict.items():
        print(f"{key}: {value}")



def read_file(filename):
    try:
        file = open(filename, "r", encoding="utf-8")
        lines = file.readlines()
        file.close()

        return lines # list

    except Exception as e:
        print(f"ERROR: Could not open/read {filename}: {e}")



def count_names(file):
    lines = read_file(file)
    # print('lines', lines)
    
    # sort the lines
    lines.sort()
    # print('sorted lines', lines)

    print(f"Reading file {filename}\n")

    # create a dictionary out of these lines 
    # where the key is the line and the value is number of occurrences
    # default occurrence is 0
    try:
        dictionary = {}
        for line in lines:
            # strip \n from the end
            if line != "\n": # file may have empty lines    
                key = line.replace("\n", "")
                if key in dictionary:
                    dictionary[key] += 1
                else:
                    dictionary[key] = 1
        print(f"There are {len(dictionary)} unique names in {file}. Their number of occurrences are as follows: \n")
        print_dict(dictionary)
        return dictionary
    except Exception as e:
        print(f"ERROR: {e}")


count_names(filename)