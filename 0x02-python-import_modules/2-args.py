#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    n = len(sys.argv)

    if n == 1:
        print('{:d} arguments.'.format(0))
    elif n == 2:
        print('{:d} argument:'.format(1))
        print('{:d}: {:s}'.format(1, sys.argv[1]))
    else:
        print('{:d} arguments:'.format(n - 1))
        for i in range(1, n):
            print('{:d}: {:s}'.format(i, sys.argv[i]))
