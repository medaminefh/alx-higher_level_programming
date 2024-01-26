#!/usr/bin/python3
"""Write a Python script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.

The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON
formatted and not empty, display the id and name like this: [<id>] <name>
Otherwise:
Display Not a valid JSON if the JSON is invalid
Display No result if the JSON is empty
You must use the package requests and sys
You are not allowed to import packages other than requests and sys
"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/users/{}'.format(sys.argv[1])
    token = sys.argv[2]
    headers = {'Authorization': 'Bearer {}'.format(token),
               'Accept': 'application/vnd.github+json',
               'X-GitHub-Api-Version': '2022-11-28'}
    res = requests.get(url, headers=headers)
    try:
        json = res.json()
        if json:
            print(json.get('id'))
    except ValueError:
        print(None)
