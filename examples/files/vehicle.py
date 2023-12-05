# Declare a vehicle class to hold info about vehicle
class Vehicle:
    # this is a constructor, it has a special name
    # in Python the very first param must be self
    def __init__(self, make = '',  model = '', engine_cc = 0, power_kw = 0):
        self.make = make
        self.model = model
        self.engine_cc = engine_cc
        self.power_kw = power_kw

    # Lets print something when somebody prints this class
    # print(Vehcile)
    def __str__(self):
        return '\nMake: {}\nModel: {}\nEngine CC: {}\nPower KW: {}\n'.format(self.make, self.model, self.engine_cc, self.power_kw)
    
    def horsepower(self):
        return self.power_kw * 1.341

    make = ''
    model = ''
    engine_cc = 0
    power_kw = 0

    # Every class has a 'constructor' so you could initialize data
