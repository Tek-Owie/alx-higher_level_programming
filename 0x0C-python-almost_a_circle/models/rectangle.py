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

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

