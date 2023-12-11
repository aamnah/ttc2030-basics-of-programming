# Exercise 9: Exception Handling
# https://gitlab.labranet.jamk.fi/ttc2030/basics-of-programming/-/blob/master/exercises/exercise09.md

"""
9.2.
[x] Make a program to try to read all the files on the root of the hard disk C on a Windows machine. (on macOS/Linux/Unix machines try to read the user's root directory). 
    [x] View files on the console. 
[x] Then try adding the file 'ayho.txt' to the root of C (on macOS/Linux/Unix to the user's root directory).
[x] What happened? Repair the program so that it does not crash.

Bonus Question: With what permissions could you add files on macOS/Linux/Unix machines to the root directory? Reply as a comment to the source code.
"""

"""
You need sudo/root/Administrator privileges to write to system drives like C:// and root directory /
"""

import os
from bcolors import color

path = '/'
filename = 'ayho.txt'

def read_files(path):
    print(f"The contents of {path} are:")
    if os.path.exists(path):
        with os.scandir(path) as entries:
            for entry in entries:
                print(entry.name)

read_files(path)

def write_file(path, filename, permissions):
    try:
        file = open(path + filename, "w")
        file.write("Files example, writing to user's home folder")
        file.close()
    except PermissionError:
        print(f"{color.FAIL}Could not create {path+filename} because you do not have permission \nto write to the {path} directory {color.ENDC}")
    except Exception as e:
        print("Failed to create file:", filename)
        print(f"ERROR: {e}")

write_file(path, filename, "w")