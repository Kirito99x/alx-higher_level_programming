#!/usr/bin/python3
#!/usr/bin/python3
"""A python script that:
- takes your GitHub username and password
- uses the GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    autho = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    re = requests.get("https://api.github.com/user", auth=autho)
    print(re.json().get("id"))
