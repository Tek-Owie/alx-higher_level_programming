#!/usr/bin/python3

def max_integer(my_list=[]):
    max_val = -float('inf')
    if not my_list:
        max_val = None
    else:
        for int in my_list:
            if int > max_val:
                max_val = int
    return max_val
