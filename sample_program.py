def ask_number(prompt):
  try:
    number = int(input(prompt))
  except:
    print('Not a number')
  return number

# ask_number('Gimme a number: ')

def print_menu():
    print('Enter selection: ')
    print('1: Go skiing')
    print('2: Stay home and eat chips')
    print('3: Get your car to the race track')
    print('4: Do your assignments')
    print('5: Netflix and Chill')
    print('0: Sleep')

# selection = 1
# while selection != 0:
#     print_menu()
#     selection = ask_number('What would you like to do? ')

#     if selection != 0: print('ok, you do that')
#     else: print("I'm gone")

while True:
    print_menu()
    selection = ask_number('What would you like to do? ')
    if selection == 0:
        print('I am gone')
        break
    elif selection < 0 or selection > 5:
        print('I do not care')
        continue
    print('Doing activity', selection)