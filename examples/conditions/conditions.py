# 08 - CONDITIONS
# https://gitlab.labranet.jamk.fi/ttc2030/basics-of-programming/-/blob/master/materials/08-conditions.md

number1 = int(input("Gimme a number: "))
if number1 == 10:
    print("number is 10")


number2 = int(input("Gimme a number: "))
if number2 == 10:
    print("number is 10")
elif number2 < 10:
    print("Number is less than 10")
elif number2 >= 20:
    print("Number is greater than or equal to 20")
else:
    print("Number is in between 11 and 19")

# If the conditional statement executes only one line, it can also be written on one line:
number3 = int(input("Gimme a number: "))
if number3 == 10: print("number is 10")


# No matter how many ands and ors you have in your condition, it only produces one boolean true/false value
number4 = int(input('Gimme another number: '))
if number4 > 0 and number4 < 10:
    print('Number is in betweeen 1 and 9')
elif number4 >= 10 or number4 == 0:
    print('Number is 10 or greater, or number is 0')

# short circuting conditions is when the condition is met before the actual code meant to run has been reached

number5 = 4
number6 = 43

# Empty condition block
if number5 > number6:
    pass # pass means do nothing. you shouldn't be getting into situations like these do.