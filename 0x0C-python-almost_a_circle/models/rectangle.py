#!/usr/bin/python3
"""This module contains the Rectangle class which
inherits from the Base class.
"""

from models.base import Base


class Rectangle(Base):
    """This class inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle class.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """Return the string representation of the rectangle."""

        return "[{}] ({}) {}/{} - {}/{}".format(self.__name__,
                                                self.id, self.__x,
                                                self.__y, self.__width,
                                                self.__height)

    @property
    def width(self):
        """Return the value of width."""

        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of width."""

        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Return the value of height."""

        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of height."""

        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Return the value of x."""

        return self.__x

    @x.setter
    def x(self, value):
        """Set the value of x."""

        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Return the value of y."""

        return self.__y

    @y.setter
    def y(self, value):
        """Set the value of y."""

        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Compute the area of the rectangle."""

        return self.__width * self.__height

    def display(self):
        """Print in stdout the Rectangle instance with the character #."""

        for i in range(self.__height):
            print('#' * self.__width)
