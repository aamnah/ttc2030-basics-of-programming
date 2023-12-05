import os.path # os.path is cross-platform, works on Windows and Unix systems both

path = os.path.expanduser("~/files-example")

if not os.path.exists(path): os.makedirs(path)
print(path)

path += "/"

print(path)

filename = "example.txt"

try:    
    file = open(path + filename, "w")
    file.write("Files example, writing to user's home folder")
    file.close()
except:
    print("Failed to create file:", filename)

# if it doesn't exist, it will create one
# if one exists, it'll destroy contents and overwrite (what "w" does)
# creates file in root of the project if no path specified
# VS code makes project folder as the root location
# if you run from the command line, it'll create it in the same dir as the script
# creating files in C:\\ won't work, permission denied

