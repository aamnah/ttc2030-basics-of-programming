number1 = 100
number2 = 0
result = number1 / number2
print("Result is ", result)


# Exception handling with try, except

try:
  number = int(input('Gimme a number'))
  print('You entered: ', number)
except ValueError as error:
  print('Unable to convert to number', error)
except Exception as ex:
  print('Something went wrong :(', ex)


try:
    numbers = [1, 2, 3, 4, 5]
    print("Last number is ", numbers[5])
except IndexError:
    print("Wrong index used in accessing list")
finally:
    print("We will come here, crash or no")

# finally is useful when you want to do something regardless of whether it was successful or not
# for example, when reading files, we always wnat to close a file, even if an error occurs while reading it.

# Format strings
print(f"Hello {number}")