#!/usr/bin/python3
"""A python script that
- fetches url: https://alx-intranet.hbtn.io/status.
- uses urlib package
"""


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        body_content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body_content)))
        print("\t- content: {}".format(body_content))
        print("\t- utf8 content: {}".format(body_content.decode('utf-8')))
