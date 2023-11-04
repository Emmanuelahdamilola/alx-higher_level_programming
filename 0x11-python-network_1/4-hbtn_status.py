#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status using requests"""
import requests

if __name__ == "__main__":
    """Main function: Fetches https://alx-intranet.hbtn.io/status using requests"""
    
    # Send an HTTP GET request to the specified URL.
    r = requests.get('https://alx-intranet.hbtn.io/status')

    # Print information about the response.
    print("Body response:")
    # Display the type of the response text.
    print("\t- type: {}".format(type(r.text)))
    # Display the content of the response text
    print("\t- content: {}".format(r.text))
