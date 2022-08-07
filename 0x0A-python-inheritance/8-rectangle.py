#!/usr/bin/python3
"""
This module features the BaseGeometry class.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Instantiates the Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initializes the recyangle class.

        :param: width(int) - positive int value of width
        :param: height(int) - positive int value of height
        :rtype: nothing.
        """

        self.integer_validator('width', width)
        self.integer_validator('height', height)

        self.__width = width
        self.__height = height
