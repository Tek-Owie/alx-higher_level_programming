#!/usr/bin/python3
"""This module contains
print_square function.
"""


def print_square(size):
    """Print a square with '#' character."""
    if type(size) != int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    print(("#" * size + "\n") * size, end="")
