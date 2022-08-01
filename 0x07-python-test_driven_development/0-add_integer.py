#!/usr/bin/python3
"""
This module contains the add_integer function.
The function accetps two int/float args and returns an int.
"""

def add_integer(a, b=98):
    """It accepts two int/float args.
    Returns the sum as an integer
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
