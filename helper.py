import calls

def getCompanyId(company):
    fltr = '?name=' + str(company)
    # try except here
    d = calls.getCompanies(fltr)
    # check if company is present
    if len(d['data']['data']) == 0:
        return 0

    return d['data']['data'][0]['id']


def checkForCompanyAccess(company):
    id = getCompanyId(company)
    if not id:
        return 0
    '''
    fltr = '?company=' + str(id)
    d = calls.getCompanyInstallations(fltr)

    # check if company is registered for the service
    if len(d['data']['data']) == 0:
        return 0
    '''
    return 1

def checkForUserAccess(company, user):
    # can't fail, placed a check already
    id = getCompanyId(company)

    fltr = '/'+str(id)+'/people?company='+id
    d = calls.getCompanies(fltr)
    for employee in d['data']['data']:
        if employee['work_email'] == user:
            return 1
    return 0

def registerCompanyForService(company):
    pass

