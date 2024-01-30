#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
from urllib.request import urlopen, Request

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    req = Request(url)

    with urlopen(url) as res:
        body = res.read().decode('utf-8')
        print('Body response:')
        print('\t- type:', type(body))
        print('\t- content:', body)
