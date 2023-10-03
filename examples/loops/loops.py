# LOOPS
# https://gitlab.labranet.jamk.fi/ttc2030/basics-of-programming/-/blob/master/examples/09-loops/loops.py
number = 10
while number >= 0:
  print(number)
  number -= 1

# Looping over ranges
for i in range(10): # i could be any valid variable name, i is just kind of typical variable name
  print('Looping range(10):', i) # goes from 0-9! ranges start from 0. 0 to 9 is 10 items

for i in range(5, 10): # range can take 2 params
  print('Looping range(5, 10):', i) # starts at 5, goes till 9. Last values is (rangeMax - 1)

for i in range(5, 100, 2): # range can take 3 params, the third param (here 2) specifies how many values to skip
  print('Looping range(5, 100, 2):', i) # starts at 5, goes till 9. Last values is (rangeMax - 1)

# range with start number and step specified
print("Running for loop with range and start and step values")
for i in range(0, 10, 2):
    print("Looping range(0,10,2):", i)


# Looping over lists
names = ['Jenny', 'Jane', 'John']
for name in names:
  print(name)

# Using break and continue
print('Running a while loop with break and continue')
number = 0
while True:
  number = int(input('0 to exit, 100 ignored: '))
  if number == 0:
    break # jumps away from the code
  if number == 100:
    print('Ignored')
    continue # jumps back to the beginning of while

  print('You entered:', number)

print('All done, coffee break')
