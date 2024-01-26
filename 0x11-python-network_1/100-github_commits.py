#!/usr/bin/python3
"""Get the 10 most recent commits from a GitHub repository
"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits?per_page=10'.format(
        sys.argv[2], sys.argv[1])
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
