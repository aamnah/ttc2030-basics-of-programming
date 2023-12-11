'''
Exercise 7 
Classes and Objects
https://gitlab.labranet.jamk.fi/ttc2030/basics-of-programming/-/blob/master/exercises/exercise07.md
'''

import random
from car import Car

# 7.4
'''
Next, create at least five random car objects from these brands: 'Audi', 'BMW', 'Ford', 'Opel', 'Skoda', 'Volvo' ja 'VW'. Cars model property can be left empty if you wish. Generate a random price for each car in range 1000-10000. Add created cars into a list-collection.
Print information of all cars into the console. Tip: use Python randint-function to implement random numbers.
'''

car_brands = ['Audi', 'BMW', 'Ford', 'Opel', 'Skoda', 'Volvo', 'VW']
cars_list = []

# use a loop to auto-generate cars and random car prices and add them to a list
for brand in car_brands:
    new_car = Car(brand, 'SomeModel', random.randint(1000, 10000))
    cars_list.append(new_car)

# use another loop to print all of the cars
for car in cars_list:
    print(car)

print() # just an empty line to make output more readable
