def show_info():
    print("I'm Utils.Info")

def subtract(x, y):
    result=round((x - y), 2) # round off to 2 decimal point
    # 6.14 after rounding, otherwise 6.1434999999999995
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

    fuel_consumed = round(((travel_distance_km / 100) * fuel_consumption), 2)
    cost = round((fuel_consumed * fuel_cost), 2)

    print(f"""
Fuel consumed: {fuel_consumed} liter
Cost: {cost} €
""")

