#!/usr/bin/python3

def no_c(my_string):
    new_list = list(my_string)
    for char in new_list:
        if char == 'c' or char == 'C':
            new_list.remove(char)
    print("{:s}".format(''.join(new_list))
