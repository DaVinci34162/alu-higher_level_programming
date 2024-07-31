#!/usr/bin/python3
"""
This script fetches the 10 most recent commits from a specified GitHub repository
and prints them in the format <sha>: <author name>.
"""
import requests
import sys

def fetch_commits(repo, owner):
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    response = requests.get(url, params={'per_page': 10})
    commits = response.json()
    for commit in commits:
        sha = commit.get('sha')
        author_name = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author_name}")

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    fetch_commits(repo, owner)
