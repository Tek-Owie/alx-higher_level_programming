#!/usr/bin/python3
"""Defines a square class."""


class Square:
    """Defines a class of square."""
    def __init__(self, size=0):
        """Initializes an instance with private attr."""
        self.size = size

    @property
    def size(self):
        """It returns the size of the square."""
        return self.__size

    @size.setter
    def size(self, size):
        """sets the size of the square."""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """Returns the area of the square."""
        return (self.__size) ** 2

    def my_print(self):
        """prints the area with #"""
        if self.__size == 0:
            print()
            return
        else:
            for j in range(self.__size):
                print('#' * self.__size)
