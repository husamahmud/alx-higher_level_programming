#!/usr/bin/python3
def multiple_returns(sentence):
    n = len(sentence)
    first_char = sentence[0] if sentence else None
    return n, first_char
