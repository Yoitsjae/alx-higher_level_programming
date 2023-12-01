#!/usr/bin/python3
"""
 module using a request that fetches https://intranet.hbtn.io/status
"""
import requests


def main():
    """
    The function that fetches https://intranet.hbtn.io/status
    """
    url = 'https://intranet.hbtn.io/status'
    r = requests.get(url)
    print('Body response:')
    print('\t- type: {}'.format(type(r.text)))
    print('\t- content: {}'.format(r.text))

if __name__ == "__main__":
    main()
