#!/usr/bin/python3
"""
This script takes in a URL, sends a GET request to the URL, and displays the
body of the response using the 'requests' library. If the response status code
indicates an error (400 or higher), it prints an error message with the status code.
"""
import requests
from sys import argv

if __name__ == "__main__":
    """
    Main function: Takes in a URL, sends a GET request to the URL, and displays the
    body of the response using the 'requests' library. If the response status code
    indicates an error (400 or higher), it prints an error 
    message with the status code.
    """
    url = argv[1]

    # Send a GET request to the specified URL.
    response = requests.get(url)

    # Check the status code of the response.
    if response.status_code >= 400:
        # If the status code indicates an error,
        # print an error message.
        print("Error code: {}".format(response.status_code))
    else:
        # If the status code is not an error,
        # display the body of the response.
        print(response.text)

