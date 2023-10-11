#!/usr/bin/python3
def weight_average(my_list=[]):
    from functools import reduce
    sum_product = reduce(lambda acc, val: acc + (val[0] * val[1]), my_list, 0)
    sum_weights = reduce(lambda acc, val: acc + val[1], my_list, 0)
    return float(sum_product / sum_weights) if sum_weights != 0 else 0
