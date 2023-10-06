#!/usr/bin/python3
def max_integer(my_list=[]):
    max_val = float('-inf')
    if not my_list:
        return None
    for num in my_list:
        max_val = num if num > max_val else max_val
    return max_val
