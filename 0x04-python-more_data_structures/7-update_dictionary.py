#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    for k in list(a_dictionary):
        if not key:
            a_dictionary.setdefault(key, value)
        a_dictionary[key] = value
    return a_dictionary
