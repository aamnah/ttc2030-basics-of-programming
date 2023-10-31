list = [5, 10, 15]
list.insert(1,7) # [5, 7, 10, 15]

print('List contents:', list)

print('List item at index -1', list[-1]) # last item i.e. 15
#print('List item at index 999', list[999]) # crash, list index out of range
#print('List item at index -6', list[-6]) # crash, out of range

# This is different from other languages. If you give negative index to other languages, it will crash

list[1] = 60
print('List contents:', list) # [5, 60, 10, 15]

print('List items at range 2:5:', list[2:5]) # values for index 3,4
# in range, index at range start/end is excluded, it will not be in the result 


list.remove(10) # removes the value 10 from the list, only the first one that was found
# .remove removes an actual value, it is not taking the index
# if many values found, only the first one will be removed

#list.remove(999) # crash, value not in list

value = list.pop(1) # takes an index, not a value
# value = list.pop(999) # crash

del list[1] # takes an index

list.clear() # empty the list.

# declare list of names and print
namelist = ["Joe", "Sally", "Liam", "Robert", "Emma", "Isabella"]
print(namelist)

# loop thru a list
for name in namelist:
  print(name)

# use 'len' function to determine list length
print('\nnamelist length is:', len(namelist))

# loop thru a list while also knowing the index
# use enumerate()
# https://docs.python.org/3/library/functions.html#enumerate
for index, name in enumerate(namelist):
  print(name, 'is at index', index)

if 'Liam' in namelist:
  print('\nYes, Liam is in namelist')
  print('\nIndex of Liam is', namelist.index('Liam'))


another_namelist = namelist # equal sign does not make a copy of variable, it is a refernce. there is only one main list at this point
another_namelist[0] = 'Roger' # will replace 'Joe' in namelist
print('\n',namelist)
print('\n',another_namelist)
# any complex Data Structure by default are passed as reference instead of as copies

yet_another_namelist = namelist.copy()
yet_another_namelist[-1] = 'Mary' # 
print(namelist)
print(yet_another_namelist)

combined_list = namelist + another_namelist # not a reference this time, + sign produces completely new list
combined_list = (namelist + another_namelist) # the entire right hand side is executed first before the assignment is used. might make sense why this is a new list