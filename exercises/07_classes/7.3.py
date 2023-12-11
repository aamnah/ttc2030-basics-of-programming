from car import Car

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
