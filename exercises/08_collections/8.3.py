# Exercise 8: Collections
# https://gitlab.labranet.jamk.fi/ttc2030/basics-of-programming/-/blob/master/exercises/exercise08.md
"""
8.3.
Implement a program that can store data for ten different cars. Car should have at least registration number (eg ABC-123) and car make (eg Skoda). Invent various registration numbers and car brands by yourself. Save the data of ten cars to the collection of your choice. Then print the car information first in alphabetical order by car brand, and then in alphabetical order by registration number.

https://docs.python.org/3/howto/sorting.html
"""

import random

class Car:
    def __init__(self, make = '', registration_number = '' ):
        self.make = make
        self.registration_number = registration_number

    def __str__(self):
        return f"{self.make}, {self.registration_number}"

    make = ''
    registration_number = ''

car_brands = ['Audi', 'BMW', 'Ford', 'Opel', 'Skoda', 'Volvo', 'VW', 'Suzuki', 'Toyota', 'Ferrari']
cars_list = []

# use a loop to auto-generate cars and random car prices and add them to a list
for brand in car_brands:
    registration_number = f"{brand[:3].upper()}-{random.randint(100, 999)}"
    new_car = Car(brand, registration_number)
    cars_list.append(new_car)

sorted_by_brand = sorted(cars_list, key=lambda car: car.make)   # sort by make
sorted_by_registration_number = sorted(cars_list, key=lambda car: car.registration_number)   # sort by registration number

print("\nSorted by Make\n---")
for car in sorted_by_brand:
    print(car)


print("\nSorted by Registration Number\n---")
for car in sorted_by_registration_number:
    print(car)

print() # just an empty line to make output more readable