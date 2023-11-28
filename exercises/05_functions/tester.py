from utils import show_info, subtract, average, calc_consumption

print()

show_info()

print()

subtract(10, 5.0) # 5.0
subtract(10, 6) # 4
subtract(10, 9.3) # 0.7 after rounding, otherwise 0.6999999999999993
subtract(10, 0) # 10
subtract(10, -1) # 11
subtract(10.12, 3.9765) # 6.14 after rounding, otherwise 6.1434999999999995

print()

average(10, 6, 8) # 8.0
average(10, 6.5, 7.5) # 8.0
average(10, -6, 8) # 4.0
average(10, 6.3, -8) # 2.8 after rounding, otherwise 2.766666666666667
average(3, 9, 13) # 8.3 after rounding, otherwise 8.333333333333334

print()

# calc_consumption(150, 1.67, 4.2)
# calc_consumption(250, 1.93, 6.3)
# Enter trip length in km: 250
# Enter fuel price/liter: 1.93
# Enter fuel consumption/100 km: 6.3
# Cost: 30.4 €