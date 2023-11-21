# Our own data type
class Computer:
    manufacturer = ''
    ram_bytes = 0 # this would be a very long number in python, memory concerns
    storage_mb = 0
    cpu = ''
    motherboard = ''

my_computer = Computer
my_computer.cpu = 'Intel Core i7'
my_computer.manufacturer = 'Jani'
my_computer.motherboard = 'Super'
my_computer.ram_bytes = 64*1024*1024*1024
my_computer.storage_mb = 500

print(my_computer) # <class '__main__.Computer'>