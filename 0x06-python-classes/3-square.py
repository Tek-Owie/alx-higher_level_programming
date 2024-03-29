#!/usr/bin/python3
"""Defines a square class."""


class Square:
    """Defines a class of square."""
    def __init__(self, size=0):
        """Initializes an instance with private attr."""
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """Returns the area of the square."""
        return (self.__size) ** 2
