'''
7.1
Declare a class Human. Class has two properties, name and age. Implement Human-class:
Constructor initializes Human-object name and age thru its parameters.
Override Human class str function to print object information.
Declare two Human class objects. Initialize them with data that produces the example output:
'''

class Human:
    def __init__(self, name = '', age = 0):
        self.name = name
        self.age = age

    def __str__(self):
        return 'Name: {}, Age: {}'.format(self.name, self.age)

    name = ''
    age = 0