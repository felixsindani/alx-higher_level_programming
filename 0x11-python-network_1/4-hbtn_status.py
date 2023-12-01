#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    """script that fetches https://alx-intranet.hbtn.io/status"""
    r = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
