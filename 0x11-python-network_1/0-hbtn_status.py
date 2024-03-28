#!/usr/bin/python3
"""Python script that fetches url
- uses urlib pakcage
"""

if __name__ == '__main__':
    import  urllib.request

    url = "http://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        body = response.read()

        print("\t- Body response:")
        print("\t- type:", type(body))
        print("\t- content:", (body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
