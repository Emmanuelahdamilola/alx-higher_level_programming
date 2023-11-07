#!/usr/bin/python3
"""Fetches GitHub user repository commits."""

import requests
from sys import argv

if __name__ == "__main__":
    # Get the GitHub username and repository name from command line arguments
    github_user = argv[1]
    github_repo = argv[2]

    # Construct the API URL for the GitHub repository's commits
    api_url = f"https://api.github.com/repos/{github_user}/{github_repo}/commits"
    
    # Send a GET request to the GitHub API to retrieve commit data
    response = requests.get(api_url)

    # Initialize a counter to limit the number of commits to display
    commit_counter = 0

    # Iterate through the commits, sorted by the author's date in descending order
    for commit in sorted(response.json(), key=lambda c: c.get('commit').get('author').get('date'), reverse=True):
        # Print the commit SHA and author's name
        print(commit.get('sha') + ": ", end="")
        print(commit.get('commit').get('author').get('name'))
        
        # Increment the commit counter
        commit_counter += 1
        
        # Limit the number of displayed commits to 10
        if commit_counter == 10:
            break

