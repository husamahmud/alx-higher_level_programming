#!/usr/bin/python3
def roman_to_int(roman_string):
    if (roman_string is None or isinstance(roman_string, str) is False):
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
             'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    prev = 0
    for i in range(len(roman_string)):
        for key, value in roman.items():
            if key == roman_string[i]:
                if value > prev and i > 0:
                    sum -= prev * 2
                    sum += value
                    prev = value
                else:
                    sum += value
                    prev = value
    return sum
