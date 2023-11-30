# Exercise 6: Recap and Debugger
# https://gitlab.labranet.jamk.fi/ttc2030/basics-of-programming/-/blob/master/exercises/exercise06.md

"""
6.2.
Create functions: cel_2_fah ja fah_2_cel
Functions take a temperature degree as parameter and convert it to between Fahrenheit and Celsius. The converted temperature value is returned to one decimal place.
Test each function by calling it with the numbers provided by the user.

For example: print(cel_2_fah(10.0)) returns value 50.0
"""

def cel_2_fah(temp_celsius):
    """converts Celsius to Fahrenheit
    """
    # Temperature in degrees Fahrenheit (°F) = (Temperature in degrees Celsius (°C) * 9/5) + 32.
    fahrenheit = (temp_celsius * 9/5) + 32
    return round(fahrenheit, 1)


def fah_2_cel(temp_fahrenheit):
    """converts Fahrenheit to Celsius
    """
    # Temperature in degrees Celsius (°C) = (Temperature in degrees Fahrenheit (°F) - 32) * 5/9.
    celsius = (temp_fahrenheit - 32) * 5/9
    return round(celsius, 1)


def tests():
    print(cel_2_fah(0)) # 32.0
    print(fah_2_cel(32)) # 0.0

    print(cel_2_fah(39)) # 102.2
    print(cel_2_fah(43)) # 109.4

    print(cel_2_fah(10.0)) # 50.0
    print(fah_2_cel(50.0)) # 10.0

# tests()

def print_menu():
    print("1: Celsius (°C) to Fahrenheit (°F)")
    print("2: Fahrenheit (°F) to Celsius (°C)")
    print()

print_menu()
conversion = int(input("What conversion would you like to do? "))
temperature = int(input("Give me a temperature value: "))

if conversion == 1:
    result = cel_2_fah(temperature)
    print(f"{temperature} °C is {result} °F")
elif conversion == 2:
    result = fah_2_cel(temperature)
    print(f"{temperature} °F is {result} °C")
