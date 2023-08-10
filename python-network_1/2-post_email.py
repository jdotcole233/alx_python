#! /usr/bin/python3
import requests
import sys
"""
    Request module demonstration comments goes here
"""

payload = {
    'email': sys.argv[2]
}

req = requests.post(sys.argv[1], data=payload)
print(req.text)