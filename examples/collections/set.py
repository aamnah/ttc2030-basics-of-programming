# No duplicate values
nameset = {"Joe", "Sally", "Liam", "Robert", "Robert","Robert", "Emma", "Isabella", "Isabella", "Isabella"}

# No order when items are shown
# No index
print("Contents of nameset is:", nameset)
# Contents of nameset is: {'Joe', 'Emma', 'Liam', 'Isabella', 'Robert', 'Sally'}

# print the contents of the set in for loop
for name in nameset:
    print(name)

# check if certain item is in the set
name = "Sally"
print(name + " is in set:", name in nameset)


# You can not edit items, but you can find and remove them
# items in set cannot be modified but can be added and removed
# use add function to add new item
nameset.add("Bella")
print("Contents of nameset after add is:", nameset)
# no idea where it will be added. middle, start, end, who knows
# we can not insert in a specific place
nameset.add("Bella")
nameset.add("Bella")
nameset.add("Bella")

print("Contents of nameset after add is:", nameset)
# Contents of nameset after add is: {'Bella', 'Liam', 'Sally', 'Joe', 'Emma', 'Robert', 'Isabella'}

nameset.add("1234")
nameset.add(1234)
print("Contents of nameset after add is:", nameset)
# Contents of nameset after add is: {'1234', 'Sally', 'Robert', 'Liam', 1234, 'Emma', 'Joe', 'Isabella', 'Bella'}

nameset.update({'Harry', 'Hermoine', 'Ron', 'Ron'})
# notice the {}
print("Contents of nameset after add is:", nameset)

# nameset.remove('Abdullah') # will crash if Abdullah is not found
# KeyError: 'Abdullah'
nameset.remove('ron') # case-sensitive, will crash if ron is not found
# KeyError: 'ron'
nameset.discard('Ron')
nameset.discard('ron') # case-sensitive
nameset.discard('Abdullah') # will not crash if Abdullah is not found
print("Contents of nameset after add is:", nameset)