#!/usr/bin/python3
"""Send a post request to a URL with an email as a
parameter, and display the"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    res = requests.post(url, data={'email': email})
    print(res.text)
