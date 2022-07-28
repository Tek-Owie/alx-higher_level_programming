#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    for k in list(a_dictionary):
        if k != key:
            a_dictionary.setdefault(key, value)
        a_dictionary[key] = value
