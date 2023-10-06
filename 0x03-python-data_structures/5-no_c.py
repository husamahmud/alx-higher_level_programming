#!/usr/bin/python3
def no_c(my_string):
    modified_str = ''
    for c in my_string:
        if c != 'c' and c != 'C':
            modified_str += c
    return modified_str
