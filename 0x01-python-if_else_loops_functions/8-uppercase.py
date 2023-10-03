#!/usr/bin/python3
def uppercase(s):
    res = ""
    for c in s:
        if ord(c) in range(97, 123):
            res += chr(ord(c) - 32)
        else:
            res += c
    print(res.format())
