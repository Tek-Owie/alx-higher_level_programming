#!/usr/bin/python3
"""This module features the BaseGeometry class."""


class BaseGeometry:
    """Instantiates BaseGeometry class"""
    
    def area(self):
        """Raise an exception that area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Return if an input is a valid int.
        
        :param: name(str) - name of input
        :param: value(int) - value
        :rtype: nothing
        """

        if type(value) != int:
            raise TypeError('{:s} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))
