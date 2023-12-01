#!/usr/bin/python3
"""displays the value of the X-Request-Id variable found in
the header of the response.
"""

if __name__ == "__main__":
    import urllib.request
    import sys

    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    # Open the URL provided as a command-line argument
    with urllib.request.urlopen(sys.argv[1]) as response:
        # Get the value of the 'X-Request-Id' header
        x_request_id = response.headers.get('X-Request-Id')

        # Print the value of 'X-Request-Id'
        print(x_request_id)
