filename = ".\example.txt"
file = open(filename, "w")
file.write("Creating a file with Python!")
file.close()

# if it doesn't exist, it will create one
# if one exists, it'll destroy contents and overwrite (what "w" does)
# creates file in root of the project if no path specified
# creating files in C:\\ won't work, permission denied