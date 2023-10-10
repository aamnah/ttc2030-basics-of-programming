'''
7.2
Declare a class Cat. Implement two properties, name and color, and a function meow. Declare two Cat objects with following information:
'''

class Cat:
    def __init__(self, name = '', color = ''):
        self.name = name
        self.color = color

    def __str__(self):
        return 'name: {}, color: {}'.format(self.name, self.color)
    
    def meow(self):
        return 'Meoooooow!'
    
    name = ''
    color = ''