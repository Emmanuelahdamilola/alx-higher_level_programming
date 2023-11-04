#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays
the body of the response (decoded in utf-8).
"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    """
    Main function: Takes in a URL and an email, sends a POST 
    request to the passed URL with the email as a parameter, and
    displays the body of the response (decoded in utf-8).
    """
    url = argv[1]

    # Create a POST request with the URL.
    post_request = urllib.request.Request(url)
    
    try:
        # Send a POST request to the URL and retrieve the response.
        with urllib.request.urlopen(post_request) as response:
            response_content = response.read()
            
            # Decode the response content from bytes to utf-8 encoded string.
            decoded_response = response_content.decode('utf-8')
            # Display the body of the response
            print(decoded_response)
    except urllib.error.HTTPError as e:
        # Handle HTTP errors and print the HTTP status code.
        print("Error code: {}".format(e.code))

