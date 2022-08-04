#!/usr/bin/python3
"""
This module contains is_same_class function.
"""


def is_same_class(obj, a_class):
    """Return True/False if the object is an instance
    of a specified class.
    """
    if type(obj) == a_class:
        return True
    return False
