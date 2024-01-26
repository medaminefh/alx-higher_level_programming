#!/usr/bin/python3
"""Module that takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response."""
import requests

url = 'https://intranet.alxswe.com/status'

if __name__ == "__main__":
    res = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(res.text)))
    print("\t- content: {}".format(res.text))
