"""
calls.py: Gets the data using the APIs exposed by Zenefits
Author: Rahul Radhakrishnan
Email: rahulrad@usc.edu
"""

import requests

get_urls = {
    "companies": "https://api.zenefits.com/core/companies"
}

myToken = '4ZUwULwgQTu8W4XUFMEd'
headers = {'Authorization': 'Bearer ' + myToken}


def getCompanies(append_str=None, include=None):
    pagination = 'starting_after=2&limit=100'
    url = get_urls['companies']
    if append_str is not None:
        url = url + '/' + append_str
    if include is not None:
        url = url + '?' + include + '&' + pagination
    else:
        url = url + '?' + pagination
    r = requests.get(url, headers=headers)
    return r.json()
