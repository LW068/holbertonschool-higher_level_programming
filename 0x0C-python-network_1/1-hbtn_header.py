#!/usr/bin/python3
""" fetch url """

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        header = response.info()
        if 'X-Request-Id' in header:
            x_request_id = header['X-Request-Id']
            print(x_request_id)
        elif response.geturl() != url:
            new_url = response.geturl()
            req = urllib.request.Request(new_url)
            with urllib.request.urlopen(req) as new_response:
                new_header = new_response.info()
                if 'X-Request-Id' in new_header:
                    x_request_id = new_header['X-Request-Id']
                    print(x_request_id)
        else:
            print(None)
