# Exercise 5: Functions
# https://gitlab.labranet.jamk.fi/ttc2030/basics-of-programming/-/blob/master/exercises/exercise05.md

"""
5.1.
Create new source file 'utils.py'.
Implement function show_info, which prints into the console "I'm Utils.Info"
Create another new source file 'tester.py', where you call function `show_info`. Verify that output of the show_info is printed to the console.
"""

def show_info():
    print("I'm Utils.Info")

def subtract(x, y):
    # subtracting floats gives a float with a lot of decimal points
    # e.g. 13.9 - 2.3 = 11.600000000000001
    result=round((x - y), 2) # round off to 2 decimal point
    print(f"{x} - {y} is: {result}")

def average(x, y, z):
    result=round((x + y + z) / 3, 1) # division produces a float
    print(f"The average of {x}, {y}, and {z} is: {result}")

def calc_consumption(travel_distance_km, fuel_cost, fuel_consumption):
    """prints to the console how many liters of fuel have been used on the way, as well as the amount of money spent on fuel

    Parameters
    -----------
    fuel_consumption : float
        Vehicle fuel consumption as liters per 100km
    fuel_cost : float
        Cost of fuel per liter
    travel_distance_km : float
        Traveled distance in kilometres
    """

    # Make sure the user provided floating point numbers (and not strings)
    # if not. cast input as float
    if type(fuel_consumption) is not float:
        fuel_consumption = float(fuel_consumption)

    if type(fuel_price) is not float:
        fuel_price = float(fuel_price)

    if type(distance_traveled) is not float:
        distance_traveled = float(distance_traveled)

    # Do the math
    fuel_consumed = round(((travel_distance_km / 100) * fuel_consumption), 2)
    cost = round((fuel_consumed * fuel_cost), 2)

    # Rounding floats can be done with round() as well as formatted strings
    # See: https://stackoverflow.com/a/6539677
    # for an explanation on unpredictable behaviour when using round() in Python
    # round(2.675, 2) gives 2.67 rather than 2.68 
    # Since Python 3.6 you can use .foramt() like below
    # print('Fuel consumed:', '{:.2f}'.format(fuel_consumed), 'liter')
    # print('Cost:', '{:.2f}'.format(cost), '€')

    print(f"""
Fuel consumed: {fuel_consumed} liter
Cost: {cost} €
""")

