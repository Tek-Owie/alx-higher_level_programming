#!/usr/bin/python3
"""
This module features is_kind-of_class function.
"""


def is_kind_of_class(obj, a_class):
    """Return a bool if the obj is an instance of a_class.

    Keyword arguments:
    obj - the object to be checked
    a_class - the class to check
    """
    if isinstance(obj, a_class):
        return True
    return False
