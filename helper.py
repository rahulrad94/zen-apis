"""
helper.py: Implements all the helper functions required by cli.py
Author: Rahul Radhakrishnan
Email: rahulrad@usc.edu
"""


import re
import calls
from tabulate import tabulate
import csv

# flattens a json into a list
def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


# removes the unnecessary elements from the list
def clean_up(jsonList):

    # regex to remove urls (Referred online)
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    # regex to remove /core/*
    regex1 = re.compile(
        r'^/core/*', re.IGNORECASE)

    # regex to remove /meta/*
    regex2 = re.compile(
        r'^/meta/*', re.IGNORECASE)

    L = []
    for ele in jsonList:
        if re.match(regex, ele) or re.match(regex1, ele) or re.match(regex2, ele):
            continue
        L.append(ele)
    return L


# returns company_id for the "test company"
def getCompanyId():
    jsonData = calls.getCompanies()
    return str(jsonData['data']['data'][0]['id'])


# displays the information in a tabular format
def display(display_list, export):
    headers = ['First', 'Last', 'Department', 'Title', 'Location', 'Manager', "Salary", 'Work Email']
    print tabulate(display_list, headers=headers)

    if export is not None:
        myFile = open(export, 'w')
        with myFile:
            writer = csv.writer(myFile)
            display_list.insert(0, headers)
            writer.writerows(display_list)
            print "Exported to the file: " + export

# displays the necessary information to the user
def extractInfo(employee_list, export):
    if len(employee_list) == 0:
        return
    display_list = []
    for employee in employee_list:
        if str(employee['first_name']) == 'Admin':
            continue
        if employee['location'] is not None:
            location = employee['location']['city']
        else:
            # assign none
            location = employee['location']

        if employee['manager'] is not None:
            manager = (str(employee['manager']['first_name']) + ' ' + str(employee['manager']['last_name']))
        else:
            # assign none
            manager = employee['manager']

        # Ambiguity here. Clarify!
        salary = None
        if employee['employments']:
            if len(employee['employments']['data']) > 0:
                salary = employee['employments']['data'][0]['annual_salary']

        details = [employee['last_name'], employee['first_name'], employee['department']['name'],
                   employee['title'], location, manager, salary, employee['work_email']]

        details = [str(i) for i in details]
        display_list.append(details)
        details=[]
    display(display_list, export)


# returns the info of all the employees of the "test company"
def getAllEmployeeDetails(company_id, export):
    append_str = str(company_id)+'/'+'people'
    includes = 'includes=department+employments+manager+location'
    jsonData = calls.getCompanies(append_str, includes)
    employee_list = jsonData['data']['data']
    extractInfo(employee_list, export)


# return the info of only the matched employees
def getEmployeeDetails(company_id, search_str, export):
    append_str = str(company_id) + '/' + 'people'
    includes = 'includes=company+department+employments+manager+location'
    jsonData = calls.getCompanies(append_str, includes)
    employee_list = jsonData['data']['data']
    process_list = []

    for employee in employee_list:
        if employee['first_name'] == 'Admin':
            continue
        jsonList = flatten_json(employee).values()
        jsonList = [str(x).lower() for x in jsonList if x is not None]
        jsonList = clean_up(jsonList)

        # edit distance is a better algorithm for this
        res = [s for s in jsonList if search_str in s]
        if len(res)>0:
            process_list.append(employee)
    extractInfo(process_list, export)