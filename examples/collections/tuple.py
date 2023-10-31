# Tuple is list-like data structure
# () instead of []
# tuple is more restrictive
# after initialization you can not modify it anymore
# it is read-only type of data
nametuple = ("Joe", "Sally", "Liam", "Robert", "Emma", "Isabella")

print("Contents of nametuple is:", nametuple)

print("Tuple item at index 1:", nametuple[1])
print("Tuple item at index -1:", nametuple[-1])

# range parameters are start index (inclusive) and end index (exclusive)
print("Tuple items at range 2:5:", nametuple[2:5])

# many times tuples are used as return values for functions
# for example for error data and such

# You can convert a list to a tuple and vice versa easily
namelist = list(nametuple) # copy, not a reference

namelist[1] = 'Ali'

nametuple = tuple(namelist)

# we didn't really modify the original, we created a copy as new one and re-assigned it as the new value

print("Contents of nametuple is:", nametuple)

# strange thing, special case
# what happens when you want to make a tuple of only 1 element
name_tuple = ('Joe')
print(type(name_tuple)) # <class 'str'>

# Add a comma at the end
name_tuple = ('Joe',)
print(type(name_tuple)) # <class 'tuple'>