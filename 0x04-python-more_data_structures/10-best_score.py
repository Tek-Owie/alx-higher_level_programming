#!/usr/bin/python3

def best_score(a_dictionary):
    highest = float(-inf)
    key = ''
    for k,v in a_dictionary.items():
        if v > highest:
            key = k
        else:
            key = None
    return key
