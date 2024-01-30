#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
from urllib.request import urlopen

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'

    with urlopen(url) as res:
        body = res.read()

    print('Body response:')
    print('- type:', type(body))
    print('- content:', body)
    print('- utf8 content:', body.decode('utf-8'))

    res.close()
