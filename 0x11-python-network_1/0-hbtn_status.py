#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import  urllib

url = "http://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    body = response.read().decode('utf-8')

print("/t- Body response:")
print("/t/t- type:", type(body))
print("/t/t- content:", (body))