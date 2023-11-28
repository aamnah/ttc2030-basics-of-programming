# Our own data type
class Computer:
    # Override the default message printed when the class is called
    # __blah__ means an internal function
    def __str__(self): # first parameter is always 'self', which is used to refer to the own data inside
        return f"Computer: {self.manufacturer}, {self.cpu} \nRAM: {self.ram_bytes} \nStorage: {self.storage_mb}"
    

    manufacturer = ''
    ram_bytes = 0 # this would be a very long number in python, memory concerns
    storage_mb = 0
    cpu = ''

my_computer = Computer() # you need the (), have to initialize it, something to do with constructor
my_computer.cpu = 'Intel Core i7'
my_computer.manufacturer = 'HP'
my_computer.ram_bytes = 64*1024*1024*1024
my_computer.storage_mb = 500

print(my_computer) 
# Computer: HP, Intel Core i7 
# RAM: 68719476736
# Storage: 500 