'''
Classes can give us our own custom data strutcures
'''

from vehicle import Vehicle

# datsun = Vehicle()
datsun = Vehicle('Datsun', '100A', 998, 12)

print(datsun) #<vehicle.Vehicle object at 0x000001F410C9E490>

""" datsun.make = 'Datsun'
datsun.model = '100A'
datsun.engine_cc = 998
datsun.power_kw = 12 """



print(datsun.make) #Datsun

# Make another vehicle, say Toyota

toyota = Vehicle('Toyota', 'Celica', 1588, 43)

print(toyota)

print('Datsun power is:', datsun.horsepower())
print('Toyota power is:', toyota.horsepower())

print('\n')