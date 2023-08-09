#! /usr/bin/python3
import requests
import sys
"""
    Request module demonstration comments goes here
"""

req = requests.get(sys.argv[1])

if req.status_code >= 400:
    print("Error code: {}".format(req.status_code))