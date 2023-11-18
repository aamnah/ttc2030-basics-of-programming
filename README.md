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

A string literal placed directly below the object can serve as documentation

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