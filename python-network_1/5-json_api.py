#! /usr/bin/python3

import requests
import sys
"""
    Request module demonstration comments goes here
"""

if len(sys.argv):
    q = ""

req = requests.post("http://0.0.0.0:5000/search_user", params={'q': q})

response = req.json()
if not response:
    print("Not a valid JSON")
    exit(1)
elif len(response) == 0:
    print("No result")
    exit(1)


print(f"[{response[id]}] {response['name']}")