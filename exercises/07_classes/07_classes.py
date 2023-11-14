'''
Exercise 7 
Classes and Objects
https://gitlab.labranet.jamk.fi/ttc2030/basics-of-programming/-/blob/master/exercises/exercise07.md
'''

import random
from human import Human
from cat import Cat
from car import Car

# 7.1
ahmed = Human('Ahmed', 23)
nora = Human('Nora', 27)

print(ahmed)
print(nora)

print() # just an empty line to make output more readable


# 7.2
kitty = Cat('Kitty', 'brown')
grumpus = Cat('Mr. Grumpus The Second', 'black')

print(kitty)
print(grumpus)

print(kitty.name, 'says:', kitty.meow())
print(grumpus.name, 'says:', grumpus.meow())

print() # just an empty line to make output more readable


# 7.3
'''
 Create at least three different car objects. Set the properties like this:

    brand="Skoda" model="Octavia" price=3000
    brand="Audi" model="A4" price=4000
    brand="Volvo" model="V70" price=5000

Print information of all cars into the console. In addition, calculate the combined price of all cars and print that into the console.
'''
car1 = Car(brand = 'Skoda', model = 'Octavia', price = 3000)
car2 = Car(brand = 'Audi', model = 'A4', price = 4000)
car3 = Car(brand = 'Volvo', model = 'V70', price = 5000)


print('car1:', car1)
print('car2:', car2)
print('car3:', car3)

print('Total price of the cars is', car1.price + car2.price + car3.price)

print() # just an empty line to make output more readable


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
