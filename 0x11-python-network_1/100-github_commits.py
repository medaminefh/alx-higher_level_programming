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
    url = 'https://api.github.com/repos/{}/{}/commits?per_page=10'.format(
        sys.argv[1], sys.argv[2])
    headers = {'Accept': 'application/vnd.github+json',
               'X-GitHub-Api-Version': '2022-11-28'}
    res = requests.get(url, headers=headers)
    try:
        json = res.json()
        if json:
            for commit in json:
                author = commit.get('commit').get('author').get('name')
                sha = commit.get('sha')
                print("{}: {}".format(sha, author))
    except ValueError:
        print(None)
