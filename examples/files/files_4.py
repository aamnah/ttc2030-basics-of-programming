import os.path # os.path is cross-platform, works on Windows and Unix systems both

path = os.path.expanduser("~/files-example")

if not os.path.exists(path): os.makedirs(path)

# print(path)
path += "/" # by default the slash at the end of the path is missing
# print(path)

filename = "example.txt"


# write multiple lines of text
filename = "multiline-text.txt"
lines = ["Line one\n", "Line two\n", "Third line\n"]

try:    
    file = open(filename, "w")
    file.writelines(lines)
    file.close()
except Exception as e:
    print("Failed to write file:", filename)
    print("Exception:", e)
finally:
    file.close()
    # this prevents files being locked and not being able to delete them


# read multiline text back from the files
lines = [""] # make sure lines is empty, get ready for fresh data
try:
    file = open(path + filename, "r")
    lines = file.readlines()
except Exception as e:
    print("Failed to read file", filename)
    print("Exception:", e)
finally:
    file.close()

print(lines)

# if it doesn't exist, it will create one
# if one exists, it'll destroy contents and overwrite (what "w" does)
# creates file in root of the project if no path specified
# VS code makes project folder as the root location
# if you run from the command line, it'll create it in the same dir as the script
# creating files in C:\\ won't work, permission denied

