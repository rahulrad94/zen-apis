import requests

get_urls = {
    "company_installations": "https://api.zenefits.com/platform/company_installs",
    "applications": "https://api.zenefits.com/platform/applications",
    "person_subscriptions": "https://api.zenefits.com/platform/person_subscriptions",
    "companies": "https://api.zenefits.com/core/companies"
}

post_urls = {
    "set_installation_status": "https://api.zenefits.com/platform/company_installs"
}


myToken = '4ZUwULwgQTu8W4XUFMEd'
headers = {'Authorization': 'Bearer ' + myToken}


def getCompanies(fltr=None):
    url = get_urls['companies']
    if fltr is not None:
        url = url + fltr
    r = requests.get(url, headers=headers)
    return r.json()


def getCompanyInstallations(fltr=None):
    url = get_urls['company_installations']
    if fltr is not None:
        url = url + fltr
    r = requests.get(url, headers=headers)
    return r.json()