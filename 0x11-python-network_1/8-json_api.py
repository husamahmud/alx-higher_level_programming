#!/usr/bin/python3
"""script that takes in a letter and send a post request"""


if __name__ == '__main__':
    import requests
    import sys

    data = {'q': sys.argv[1] if len(sys.argv) > 1 else ""}
    res = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        res = res.json()
        if len(res) == 0:
            print('No result')
        else:
            print(f'[{res.get("id")}] {res.get("name")}')
    except ValueError:
        print('Not a valid JSON')
