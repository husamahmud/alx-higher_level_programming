#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx not in my_list:
        return my_list
    modified_list = my_list.copy()
    modified_list[idx] = element
    return modified_list
