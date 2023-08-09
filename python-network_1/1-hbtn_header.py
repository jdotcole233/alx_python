"""
    Request module demonstration comments goes here
    Request module demonstration comments goes here
"""
#! /usr/bin/python3

import requests
import sys

req = requests.get(sys.argv[1])
print(req.headers['X-Request-Id'])


