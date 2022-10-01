#!/usr/bin/python3
# square.py
"""
This module contains the Square class which 
inherits from the Rectangle class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent the Square class which inherit from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance.
        Args:
            size - positive integer
            x - positive integer
            y - positive integer
            id - positive integer
        """
        super().__init__(size, size, x, y, id)


    @property
    def size(self):
        """Return the size of a sqaure instance."""
        return self.width


    @size.setter
    def size(self, value):
        """Set the value of width and height of the square.
            Args:
                value (int) - the height/width of the square
            Return:
                None.
        """
        self.width = value
        self.height = value


    def __str__(self):
        """Return a str representation of the Square instance."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
