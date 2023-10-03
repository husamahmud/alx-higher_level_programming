#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
n = (number % 10) if number > 10 else -(-number % 10)

if n > 5:
    print(f'Last digit of {number:d} is {n:d} and is greater than 5')
elif n == 0:
    print(f'Last digit of {number:d} is {n:d} and is 0')
else:
    print(f'Last digit of {number:d} is {n:d} and is less than 6 and not 0')
