#!/usr/bin/python3
"""A python script that:
- takes in  URL,
- sends request to the URL then displays the value
- of the X-Request-Id found in the header of response.
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        print(dict(res.headers).get("X-Request-Id"))
