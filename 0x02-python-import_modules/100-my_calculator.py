#!/usr/bin/python3

def my_calculator(a, op, b):
    if op == "+":
        print('{} + {} = {}'.format(a, b, add(a, b)))
    elif op == "-":
        print('{} - {} = {}'.format(a, b, sub(a, b)))
    elif op == "*":
        print('{} * {} = {}'.format(a, b, mul(a, b)))
    elif op == "/":
        print('{} / {} = {}'.format(a, b, div(a, b)))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)


if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    from sys import argv

    n = len(argv)

    if n != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    my_calculator(int(argv[1]), argv[2], int(argv[3]))
