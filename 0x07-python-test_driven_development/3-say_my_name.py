#!/usr/bin/python3
"""This module contains 
the say_my_name function
"""


def say_my_name(first_name, last_name=""):
    """Return first_name and last_name
    :first_name - str arg
    :last_name - str arg
    :type - str
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string ')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string ')
    print("My name is", first_name, last_name)

