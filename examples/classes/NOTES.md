# Class

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