#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request and displays
the value of the X-Request-Id variable found in the header
"""


if __name__ == '__main__':
    from urllib.request import Request, urlopen
    from sys import argv

    req = Request(argv[1])
    with urlopen(req) as res:
        header = res.info()
        print(header['X-Request-Id'])
