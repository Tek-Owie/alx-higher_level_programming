#!/usr/bin/python3
"""This module contains the Rectangle class which
inherits from the Base class.
"""

from models.base import Base


class Rectangle(Base):
    """This class inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle class."""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

