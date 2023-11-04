#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL, and displays the
value of the X-Request-Id variable found in the header of the response.
"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    """Main function: Takes in a URL, sends a request to the URL, and displays
    the value of the X-Request-Id variable found in the header of the response."""
    
    # Open a connection to the URL provided as a command-line argument.
    with urllib.request.urlopen(argv[1]) as response:
        # Extract the 'X-Request-Id' header from the response's headers.
        html_id = response.info().get('X-Request-Id')
        
        # Print the value of the 'X-Request-Id' header.
        print(html_id)
