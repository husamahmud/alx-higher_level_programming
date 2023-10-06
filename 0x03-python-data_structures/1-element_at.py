#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx not in my_list:
        return 'None'
    return '{:d}'.format(my_list[idx])
