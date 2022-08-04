#!/usr/bin/python3
"""This module contains inherits_from function."""


def inherits_from(obj, a_class):
    """Return a bool if obj is a subclass of a_class.

    Keyword arguments:
    obj - the object to be checked
    a_class - the class to check
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
