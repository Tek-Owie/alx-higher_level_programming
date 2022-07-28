#!/usr/bin/python3

def best_score(a_dictionary):
    highest = -float('inf')
    key = None
    for k,v in a_dictionary.items():
        if v > highest:
            highest = v
            key = k
    return key
