# Exercise 5: Functions
# https://gitlab.labranet.jamk.fi/ttc2030/basics-of-programming/-/blob/master/exercises/exercise05.md

"""
5.3.
Add function calc_consumption into the 'utils.py' file. calc_consumption takes parameters:

Vehicle fuel consumption as liters per 100km
Cost of fuel per liter
Traveled distance in kilometres.

The calc_consumption function prints to the console how many liters of fuel have been used on the way, as well as the amount of money spent on fuel.
Create a file 'consumption.py' asking the user: consumption, fuel price and distance traveled. Then call the calc_consumption function from the program. Check that the function calculates consumption and fuel price correctly.

Example output:

  Enter trip length in km: 150
  Enter fuel price/liter: 1.67
  Enter fuel consumption/100 km: 4.
  Fuel consumed: 6.30 liter
  Cost: 10.52 €
"""

from utils import calc_consumption

travel_distance_km = input("\nEnter trip length in km: ")
fuel_cost = input("Enter fuel price/lite: ")
fuel_consumption = input("Enter fuel consumption/100 km: ")

calc_consumption(travel_distance_km, fuel_cost, fuel_consumption)