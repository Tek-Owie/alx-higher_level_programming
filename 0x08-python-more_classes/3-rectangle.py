#!/usr/bin/python3
"""Defines the class of Rectangle."""


class Rectangle:
    """Defines the class of rectangle"""
    def __init__(self, width=0, height=0):
        """Instantiates the rectangle with dimensions."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of width."""
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """Returns the value of height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
    
    def __str__(self):
        """Prints the rectangle with #."""
        string = ''
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width 
                                for j in range(self.__height))
        return string
