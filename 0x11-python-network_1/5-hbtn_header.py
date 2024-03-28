#!/usr/bin/python3
"""Displays X-Request-Id header variable of a request"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    re = requests.get(url)
    print(re.headers.get("X-Request-Id"))
