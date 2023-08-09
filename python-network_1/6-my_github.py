#! /usr/bin/python

import requests
import sys
"""
    Request module demonstration comments goes here
"""

header = {
    "X-GitHub-Api-Version":"2022-11-28",
    "Accept": "application/vnd.github+json",
    "Authorization" : "Bearer " + sys.argv[2]
}

req = requests.get("https://api.github.com/user", headers=header)
print(req.json()["id"])