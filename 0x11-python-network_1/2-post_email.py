#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response"""
from urllib.request import urlopen, Request
from urllib.parse import urlencode

from sys import argv

if __name__ == '__main__':
    url = argv[1]
    email = argv[2]

    data = urlencode({'email': email}).encode('utf-8')
    req = Request(url, data=data, method='POST')

    with urlopen(req) as res:
        body = res.read().decode('utf-8')
        print('Your email is:', body)
