from utils import calc_consumption

travel_distance_km = float(input("\nEnter trip length in km: "))
fuel_cost = float(input("Enter fuel price/lite: "))
fuel_consumption = float(input("Enter fuel consumption/100 km: "))

calc_consumption(travel_distance_km, fuel_cost, fuel_consumption)