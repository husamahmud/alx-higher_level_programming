#!/usr/bin/python3
def uppercase(s):
    res = ""
    for c in s:
        if ord(c) in range(97, 123):
            res += c.upper()
        else:
            res += c
    print(res.format())
