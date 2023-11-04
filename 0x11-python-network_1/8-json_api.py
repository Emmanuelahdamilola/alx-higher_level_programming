#!/usr/bin/python3
"""
This script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter using the 'requests' library.
It processes the response and displays the results or error messages.
"""
import requests
from sys import argv

if __name__ == "__main__":
    """
    Main function: Takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter using the 'requests' library.
    It processes the response and displays the results or error messages.
    """
    url = 'http://0.0.0.0:5000/search_user'

    # Determine whether the letter is provided as a command-line argument.
    if len(argv) == 2:
        letter = argv[1]
    else:
        letter = ""

    # Send a POST request with the 'q' parameter.
    response = requests.post(url, data={'q': letter})

    try:
        # Try to parse the JSON response.
        response_json = response.json()
        
        if response_json:
            # If JSON is not empty, display the ID and Name.
            print("[{}] {}".format(response_json.get('id'), response_json.get('name')))
        else:
            # If JSON is empty, display 'No result'.
            print("No result")
    except:
        # If the JSON is invalid or any error
        # occurs, display 'Not a valid JSON'.
        print("Not a valid JSON")
