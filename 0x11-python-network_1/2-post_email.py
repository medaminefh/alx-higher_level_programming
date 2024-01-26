#!/usr/bin/python3
"""Module that takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response."""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': sys.argv[2]}).encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
