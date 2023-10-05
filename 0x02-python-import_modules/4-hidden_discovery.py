#!/usr/bin/python3
if __name__ == '__main__':
    names = dir(hidden_4.pyc)
    for name in names:
        if name[:2] != '__':
            print('{:s}'.format(name))
