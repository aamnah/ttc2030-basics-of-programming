"""
Strings
"""
first_name = 'Amna'
last_name = 'Akram'
full_name = first_name + last_name

print(full_name)

age = 26
group = 'TIC23S1'
bio = 'First name: {}\nLast name: {}\nAge: {}\nGroup: {}'.format(first_name, last_name, age, group)

print(bio)

# Strings are like arrays
text = 'ABC'
a = text[0]
b = text[1]
c = text[2]

print('The second character is ' + b )

print('Text length is ' + str(len(text)) + ' characters')

"""
User Input
"""
line = input('Enter a line of text: ')
print('You entered ' + line)

user_number = input('Give me a number: ')
print('User entered: ', int(user_number))