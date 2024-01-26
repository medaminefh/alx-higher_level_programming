#!/usr/bin/python3
"""Fetches https://intranet.alxswe.com/status"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.alxswe.com/status') as res:
        data = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(data.decode('utf-8')))
