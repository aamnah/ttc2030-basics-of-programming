def safe_division(x, y):
  if y == 0:
    raise Exception('Exception from safe division')
  return x / y  

try:
  result = safe_division(100, 0)
#except:
#  print('safe_division raised an error') # safe_division raised an error 
except Exception as error: # this will give you the original exception from the function
  # otherwise, it will show you the message from this exception for try/except
  print('safe_division raised an error: ', error) # safe_division raised an error: Exception from safe division

def someday_something_here():
  raise NotImplementedError('This function is not implemented yet')

someday_something_here()