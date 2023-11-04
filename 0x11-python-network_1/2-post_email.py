#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response (decoded in utf-8).
"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    """
    Main function: Takes in a URL and an email, sends a POST request to the passed
    URL with the email as a parameter, and displays the body of the response (decoded in utf-8).
    """
    # Extract the URL and email from command-line arguments.
    url = argv[1]
    email = argv[2]

    # Create a dictionary with 'email' as a parameter and encode it.
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')

    # Create a POST request with the URL and encoded data.
    req = urllib.request.Request(url, data)

    # Send the POST request and retrieve the response.
    with urllib.request.urlopen(req) as response:
        html = response.read()
        html_str = html.decode('utf-8')

    # Display the body of the response (decoded in utf-8).
    print(html_str)

