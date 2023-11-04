#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL, and displays the
value of the X-Request-Id variable found in the header of the response
using the 'requests' library.
"""
import requests
from sys import argv

if __name__ == "__main__":
    """
    Main function: Takes in a URL, sends a request to the URL, and displays
    the value of the X-Request-Id variable found in the header of the response
    using the 'requests' library.
    """
    
    # Send an HTTP GET request to the URL provided
    # as a command-line argument.
    response = requests.get(argv[1])

    try:
        # Try to retrieve the 'X-Request-Id' header from the response.
        x_request_id = response.headers['X-Request-Id']
        
        # Display the 'X-Request-Id' value found in the header.
        print(x_request_id)
    except:
        # If the header is not found, do nothing (pass).
        pass

