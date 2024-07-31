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

if __name__ == "__main__":
    url = 'https://alu-intranet.hbtn.io/status'
    fetch_status(url)
