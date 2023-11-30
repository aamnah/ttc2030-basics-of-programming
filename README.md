# Basics Of Programming

- [Course Material](https://gitlab.labranet.jamk.fi/ttc2030/basics-of-programming/-/tree/master/materials)


NOTES
- `Z:\` drive aka `(\\storage\homes)`  follows you around the network, can be slow. _My Documents_ is also saved in `Z:\` drive
- `D:\` drive is local to the computer. Faster drive, but files stay on the one particular computer that you were using at the time



Class is a type, and an object is in memory.


### VS Code settings for Python

Set Default Formatter and Tab Size 4
```json
  "[python]": {
    "editor.tabSize": 4,
    "editor.formatOnType": true,
    "editor.formatOnSave": true,
    "editor.wordBasedSuggestions": false,
    "diffEditor.ignoreTrimWhitespace": false,
    "editor.defaultFormatter": "ms-python.python",
  }
```

### Documenting Python Code

A string literal placed directly below the object can serve as documentation. [Read more](https://realpython.com/documenting-python-code/)

```py
def plus_one(x):
    """purpose of this function is to increase the given parameter by one
    
    Parameters
    ----------
    x : int
      a numeric value that will be increased by one

    Returns
    -------
    int
      increases value of parameter 'x' by one and returns the result
    """
    result = x + 1
    print(result)
    return result

plus_one(99)
```

## Variables

Variable names can NOT
- start with a number (e.g. `1msg`)
- have a space in the name (e.g. 'super msg')
- have a '-' in the name (e.g. 'super-msg')

You can not declare a variable without initializing it. For example:

This is fine:

```py
super_msg = 'Amna is super'
```

While this is not:

```py
super_msg

super_msg = 'Amna is super'
```

Q: If you have multiple values for the same variable, what will happen? 
A: The last one will overwrite the one before

## Conditions

```py
number2 = int(input("Gimme a number: "))
if number2 == 10:
    print("number is 10")
elif number2 < 10:
    print("Number is less than 10")
elif number2 >= 20:
    print("Number is greater than or equal to 20")
else:
    print("Number is in between 11 and 19")
```

having the statements on the same line is also valid, but you can not have `if` and `else` on the same line

```py
# having them on the same line is also valid
number2 = int(input("Gimme a number: "))
if number2 == 10: print("number is 10")
elif number2 < 10: print("Number is less than 10")
elif number2 >= 20: print("Number is greater than or equal to 20")
else: print("Number is in between 11 and 19")
```

You can also have `not` in `if` statements

```py
number2 = int(input("Gimme a number: "))
if not number2 == 10: print("number is not 10")
elif not number2 < 10: print("Number is not less than 10")
elif number2 >= 20: print("Number is greater than or equal to 20")
else: print("Number is in between 11 and 19")
```

## Logical operations
```
OR
1010
0101

= 1111
```

```
AND
1010
0101

= 0000
```

```
XOR (NOT OR / Exclusive OR)
1010
0101

= 0000
```

## Collections

```py
# List
namelist = ["Joe", "Sally", "Liam", "Robert", "Emma", "Isabella"]

# Tuple
# read-only
nametuple = ("Joe", "Sally", "Liam", "Robert", "Emma", "Isabella")
single_nametuple = ("Joe",)

# Set
# no order or index, no duplicates
# can not edit items, but can add/delete
nameset = {"Joe", "Sally", "Liam", "Robert", "Emma", "Isabella"}

# Dictionary
# Key-value pair collection
bookdict = {
    12345678: "Book 1",
    12345679: "Book 2",
    12345680: "Book 3",
    12345681: "Book 4",
    12345682: "Book 5",
}
```


### Set
No order of items, which means there is no index

## Class

Class constructor

```python
  # this is a constructor, it has a special name
  # in Python the very first param must be self
  def __init__(self, make = '',  model = '', engine_cc = 0, power_kw = 0):
    self.make = make
    self.model = model
    self.engine_cc = engine_cc
    self.power_kw = power_kw
```

### Converting an Array to a String

```py
num = [2,7,12,19,27,33,38]

print(" ".join(str(e) for e in num)) # 2 7 12 19 27 33 38
print(",".join(str(e) for e in num)) # 2,7,12,19,27,33,38
```

## Exceptions
Exeptions let you move on with your code instead of crashing. You `try` and if that doesn't work, it goes to the `exception`, where you can _handle_ it.

For example, when input is not given in the right format, tell the user with an exception.

```py
def ask_number(prompt):
  try:
    number = int(input(prompt))
  except:
    print('Not a number')
  return number

ask_number('Gimme a number: ')
```

## Doing maths in Python
[read more on Using Python as a Calculator](https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator)

Rounding decimal places
- [How can I format a decimal to always show 2 decimal places?](https://stackoverflow.com/questions/1995615/how-can-i-format-a-decimal-to-always-show-2-decimal-places)
- [Limiting floats to two decimal points](https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points/6539677#6539677)
- round(float_num, num_of_decimals)

- subtracting floats gives a float with a lot of decimal points (16)
- division always returns a float

```py
# Subtracting floats
13.9 - 2.3 = 11.600000000000001
12.4 - 8.0 = 4.4
12.4 - 8.1 = 4.300000000000001
```

```py
# Division
9 / 3 = 3.0
5 / 2 = 2.5
5 / 3 = 1.6666666666666667
```