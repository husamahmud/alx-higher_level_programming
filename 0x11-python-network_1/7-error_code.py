#!/usr/bin/python3
"""fetch an url using requests package and display the variable from header"""

if __name__ == '__main__':
    import requests
    import sys

    res = requests.get(sys.argv[1])
    if res.status_code >= 400:
        print(f'Error code: {res.status_code}')
    else:
        print(res.text)
