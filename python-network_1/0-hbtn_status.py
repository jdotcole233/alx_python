#! /usr/bin/python
import requests
"""
    Request module demonstration comments goes here
"""

request = requests.get('https://alu-intranet.hbtn.io')
print("Body response:", end="\n")
print(f"\t- type: {type(request.text)}")
print(f"\t- content: {request.text}")