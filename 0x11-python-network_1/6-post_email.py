#!/usr/bin/python3
"""A  python script that:
- takes in URL and email,
- sends a post request to URL with the email and displays the value response.
"""
import sys
import request

if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}

    re = requests.post(url, data=value)
    print(re.text)

