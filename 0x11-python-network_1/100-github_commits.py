#!/usr/bin/python3
"""display the id variable found in the header of the response."""

if __name__ == "__main__":
    import requests
    import sys

    url = f'https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits'
    req = requests.get(url)
    res = req.json()
    for commit in res[:10]:
        print(f'{commit.get("sha")}: '
              f'{commit.get("commit").get("author").get("name")}')
