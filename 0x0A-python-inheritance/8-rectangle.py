#!/usr/bin/python3
"""This module features the BaseGeometry class."""


class BaseGeometry:
    """Instantiates BaseGeometry class"""
    
    def area(self):
        """Raise an exception that area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Return if a value is not an int, nor less than 0.
        
        :param: name (str) - name of input value.
        :param: value(int) - input value to be validated.
        :rtype: exception (value or type errors)
        """
        if type(value) != int:
            raise TypeError('{:s} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """Instantiates the Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initializes the recyangle class.

        :param: width(int) - positive int value of width
        :param: height(int) - positive int value of height
        :rtype: nothing.
        """

        if BaseGeometry.integer_validator(self, 'width', width) \
            BaseGeometry.integer_validator(self, 'height', height):
                self.__width = width
                self.__height = height
