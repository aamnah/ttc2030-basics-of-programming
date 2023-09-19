# This is a comment
import datetime

'''
this is a multi-line block comment
'''

"""
this is a multi-line block comment
"""

print(datetime.datetime.now())


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

#plus_one(99)

