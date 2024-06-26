#!/usr/bin/python3
"""A python script that
- fetches the url https://alx-intranet.hbtn.io/status.
- uses the urlib package
"""


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as re:
        body = re.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
