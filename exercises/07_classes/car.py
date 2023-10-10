'''
7.3
You have three cars in your garage. Declare a class Car. Car has three properties; brand, model and price. Create at least three different car objects. Set the properties like this:

    brand="Skoda" model="Octavia" price=3000
    brand="Audi" model="A4" price=4000
    brand="Volvo" model="V70" price=5000

Print information of all cars into the console. In addition, calculate the combined price of all cars and print that into the console.
'''

class Car:
    def __init__(self, brand = '', model = '', price = 0):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return '{} {} {}'.format(self.brand, self.model, self.price)

    brand = ''
    model = ''
    price = 0