#!/usr/bin/python3
"""
This script lists the 10 most recent commits (from the most recent to oldest)
of the repository "rails" by the user "rails" on GitHub.
"""
import requests
from sys import argv

if __name__ == "__main__":
    """
    Main function: Lists the 10 most recent commits (from the most recent to oldest)
    of the repository "rails" by the user "rails" on GitHub.
    """
    repository_name = argv[1]
    owner_username = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner_username, repository_name)

    # Send a GET request to the GitHub API to retrieve commit information.
    response = requests.get(url)
    commit_list = response.json()

    try:
        # Iterate through the first 10 commits and
        # print the SHA and author's name.
        for i in range(10):
            commit = commit_list[i]
            sha = commit.get('sha')
            author_name = commit.get('commit').get('author').get('name')
            print("{}: {}".format(sha, author_name))
    except:
        # Handle exceptions (e.g., fewer than 10 commits) and do nothing (pass).
        pass

