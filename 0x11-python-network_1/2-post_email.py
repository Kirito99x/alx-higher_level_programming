#!/usr/bin/python3
"""A python script that:
- takes in a URL
- sends a POST request to the passed URL
- takes email as a param
- displays the body response
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = {"your email is": sys.argv[2]}
    body = urllib.parse.urlencode(email).encode("ascii")

    request = urllib.request.Request(url, body)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))