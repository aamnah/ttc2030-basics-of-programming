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
