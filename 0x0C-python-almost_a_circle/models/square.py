#!/usr/bin/python3
#square.py
"""
This module contains the Square class which 
inherits from the Rectangle class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherit from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance.
        Args:
            size - positive integer
            x - positive integer
            y - positive integer
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a str representation of the Square instance."""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.size)
