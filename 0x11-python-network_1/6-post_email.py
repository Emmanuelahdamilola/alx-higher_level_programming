#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
(decoded in utf-8) using the 'requests' library.
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    Main function: Takes in a URL and an email, sends a POST request to the passed
    URL with the email as a parameter, and displays the body of the response
    (decoded in utf-8) using the 'requests' library.
    """
    url = argv[1]

    # Sends a POST request with the email parameter to the URL.
    response = requests.post(url, data={'email': argv[2]})

    # Displays the body of the response (decoded in utf-8).
    print(response.text)

