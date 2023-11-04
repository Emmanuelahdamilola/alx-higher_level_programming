#!/usr/bin/python3
"""
This script takes your GitHub credentials (username and personal access token) and uses the GitHub API
to display your user ID.
"""
import requests
from sys import argv

if __name__ == "__main__":
    """
    Main function: Takes your GitHub credentials (username and personal access token) and uses the GitHub API
    to display your user ID.
    """
    # Retrieve your GitHub username and personal access token
    # from command-line arguments.
    github_username = argv[1]
    p_access_token = argv[2]

    # Set the GitHub API endpoint for user details.
    github_api_url = 'https://api.github.com/user'

    # Send a GET request to the GitHub API with Basic Authentication.
    response = requests.get(github_api_url, auth=(github_username, p_access_token))

    try:
        # Try to parse the JSON response and display user ID.
        user_data = response.json()
        print(user_data.get('id'))
    except:
        # If an exception occurs, do nothing (pass).
        pass

