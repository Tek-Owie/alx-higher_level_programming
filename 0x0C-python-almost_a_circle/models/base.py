#!/usr/bin/python3
"""
This module contains the Base class.
This class will be the 'base' of all other classes in this project.
"""


class Base:
    """Manage the id attribute in all future classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
