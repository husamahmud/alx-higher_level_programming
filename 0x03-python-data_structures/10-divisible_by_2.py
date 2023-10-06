#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    n = len(my_list)
    res = [False] * n

    for i in range(n):
        res[i] = True if my_list[i] % 2 == 0 else False

    return res
