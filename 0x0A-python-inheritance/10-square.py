#!/usr/bin/python3
"""
This module features the Square class.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Instantiates the Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initializes the recyangle class.

        :param: width(int) - positive int value of size
        :rtype: nothing.
        """

        BaseGeometry.integer_validator(self, 'size', size)

        self.__size = size

    def area(self):
        """Return the area of the square

        :param - self
        :rtype - area (integer)
        """

        return self.__size ** 2
