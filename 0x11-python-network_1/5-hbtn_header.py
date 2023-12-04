#!/usr/bin/python3
"""
Takes in a URL, sends a request, and displays the value of the variable
X-Request-Id in the response header using the requests and sys packages.
"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    response = requests.get(url)

    # Get the value of X-Request-Id from the response headers
    x_request_id = response.headers.get('X-Request-Id')

    print(x_request_id)
