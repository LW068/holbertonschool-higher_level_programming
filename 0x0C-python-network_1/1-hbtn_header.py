#!/usr/bin/python3
""" fetch url """

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        header = response.info()
        x_request_id = header.get('X-Request-Id')
        print(x_request_id)
