#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_cpy = my_list[:]
    if idx < 0 or len(my_list) - 1 < idx:
        return list_cpy
    list_cpy[idx] = element
    return list_cpy
