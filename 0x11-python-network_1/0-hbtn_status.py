#!/usr/bin/python3
# This script fetches the status and displays the response.

# Import the urllib.request module to make HTTP requests.
import urllib.request


if __name__ == "__main__":
    # Open a connection to the specified URL.
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        # Read the content of the response into a variable.
        html = response.read()

        # Decode the response content from bytes to a UTF-8 encoded string.
        html_str = html.decode('utf-8')

    # Print information about the response.
    print("Body response:")

    # Display the type ofthe response object (bytes).
    print("\t- type: {}".format(type(html)))
    # Display the raw content as bytes.
    print("\t- content: {}".format(html))

    # Display the content as a UTF-8 string.
    print("\t- utf8 content: {}".format(html_str))
