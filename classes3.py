# Our own data type
class Computer:
    # What values can be passed, and what values would they correspond to inside the class
    def __init__(self, cpu, manu, ram_gb, storage):
        self.cpu = cpu
        self.manufacturer = manu
        self.ram_bytes = ram_gb * 1024 * 1024 * 1024
        self.storage_mb = storage

    # Override the default message printed when the class is called
    # __blah__ means an internal function
    def __str__(self): # first parameter is always 'self', which is used to refer to the own data inside
        return f"Computer: {self.manufacturer}, {self.cpu} \nRAM: {self.ram_bytes} \nStorage: {self.storage_mb}"
    
    def ram_gigabytes(self):
        return self.ram_bytes / 1024 / 1024 / 1024

    # Default values
    manufacturer = ''
    ram_bytes = 0 # this would be a very long number in python, memory concerns
    storage_mb = 0
    cpu = ''

# you need the (), have to initialize it, something to do with constructor
my_computer = Computer('Intel Core i7', 'HP', 64, 500) # initialize, because now we have an init function

print(my_computer) 
# Computer: HP, Intel Core i7 
# RAM: 68719476736
# Storage: 500 
print(my_computer.ram_gigabytes()) 