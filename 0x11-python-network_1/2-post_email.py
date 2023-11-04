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
    email_data = {'email': email}
    email_encoded = urllib.parse.urlencode(email_data)
    email_encoded = email_encoded.encode('ascii')

    # Create a POST request with the URL and encoded email data.
    request = urllib.request.Request(url, email_encoded)

    # Send the POST request and retrieve the response.
    with urllib.request.urlopen(request) as response:
        response_body = response.read()
        response_body_str = response_body.decode('utf-8')

    # Display the body of the response (decoded in utf-8).
    print(response_body_str)

