#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response"""
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv

if __name__ == '__main__':
    data = {'email': argv[2]}
    req = Request(argv[1], urlencode(data).encode('utf-8'))

    with urlopen(req) as res:
        body = res.read().decode('utf-8')
        print('Your email is:', body)
