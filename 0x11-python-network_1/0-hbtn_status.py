#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import urllib.request

    # Open the URL
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        # Read the content of the response
        content = response.read()

        # Print information about the response
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
