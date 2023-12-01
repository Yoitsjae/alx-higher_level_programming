#!/usr/bin/python3
"""
This script that fetches https://intranet.hbtn.io/status
"""
import urllib.request


def main():
    """
    funtion to print a response of a specific URL
    """
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode('utf8')))

if __name__ == "__main__":
    main()
