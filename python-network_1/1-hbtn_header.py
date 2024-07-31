import urllib.request
import sys

def fetch_request_id(url):
    with urllib.request.urlopen(url) as response:
        headers = response.getheaders()
        for header in headers:
            if header[0] == 'X-Request-Id':
                print(header[1])

if __name__ == "__main__":
    url = sys.argv[1]
    fetch_request_id(url)
