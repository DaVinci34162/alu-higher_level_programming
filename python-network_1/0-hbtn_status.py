#!/usr/bin/python3
"""
This script fetches https://alu-intranet.hbtn.io/status
using urllib package and displays the response body.
"""
import urllib.request

def fetch_status(url):
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body.decode('utf-8'))

url = 'https://intranet.hbtn.io/status'
if __name__ == "__main__":
    url = 'http://0.0.0.0:5050/status'
    fetch_status(url)
