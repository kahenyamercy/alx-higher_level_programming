#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with email as parameter,
and displays the body of the response (decoded in utf-8).
"""

if __name__ == "__main__":
    import urllib.parse
    import urllib.request
    import sys

    # Check if both URL and email are provided
    if len(sys.argv) < 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare data for POST request
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')

    # Send POST request
    with urllib.request.urlopen(url, data) as response:
        # Read and decode the content of the response
        content = response.read().decode('utf-8')

        # Print the body of the response
        print(content)
