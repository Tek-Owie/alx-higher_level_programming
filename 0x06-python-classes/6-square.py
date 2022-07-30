#!/usr/bin/python3
"""Defines a square class."""


class Square:
    """Defines a class of square."""
    def __init__(self, size=0, position=(0,0)):
        """Initializes an instance with private attr."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """It returns the size of the square."""
        return self.__size

    @property
    def position(self):
        """It returns the position of the square."""
        return (self.__position)

    @size.setter
    def size(self, size):
        """sets the size of the square."""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    @position.setter
    def position(self, position):
        """sets the position of the square."""
        if type(position) is not tuple or len(position) != 2 or \
           type(position[0]) is not int or position[0] < 0 or \
           type(position[1]) is not int or position[1] < 0:
                raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = position

    def area(self):
        """Returns the area of the square."""
        return (self.__size) ** 2

    def my_print(self):
        """prints the area with #"""
        if self.__size == 0:
            print()
            return
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(" " * self.__position[0], end='')
                print('#' * self.__size)
