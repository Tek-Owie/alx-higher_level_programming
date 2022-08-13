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

    def area(self):
        """Return the area of the rectangle.

        :param - self
        :rtype - area (integer)
        """

        return self.__width * self.__height

    def __print__(self):
        """Print the rectangle description.

        :param - self
        :rtype - string description of rectangle
        """

        print("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))

    def __str__(self):
        """Return the string description of the rectangle.

        :param - self
        :rtype - string description of rectangle.
        """

        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
