# get the company's code using the company's name
# use the code and set the status to Ok
# make sure all the employees are set properly

#!/usr/bin/python

import helper
import sys


class cli:
    company = ""
    user = ""

    def __init__(self, u, c):
        self.company = c
        self.user = u

    def show(self):
        print "Available commands\n" \
              "help- displays this menu\n" \
              "done- get me out of here!\n" \
              "listall- list all the employee details\n" \
              "string(str)- matches\n"

    def runCli(self):
        while 1:
            #use switch statement here
            user_input = raw_input("cli> ")
            if user_input == "done":
                break
            if user_input == "help":
                self.show()

    def start(self):
        company_access = helper.checkForCompanyAccess(self.company)

        if not company_access:
            print "Company not present. Is the name correct?"
            return 0

        user_access = helper.checkForUserAccess(self.company, self.user)

        if not user_access:
            print "User is either not present/doesn't have access"
            return 0


        self.runCli()

        '''
        else:
            user_input = raw_input('Do you want to register for the service?(yes/no): ')
            user_input.lower()
            if user_input[0] == 'n':
                print "Not registered for this service! Sorry."
                return 0
            helper.registerCompanyForService(self.company)
            # post
            #
        '''
        return 1

def _usage():
    print "Error!!"
    print "       Usage: python runner.py <email> <company_name>"


if __name__ == "__main__":
    args = sys.argv
    if len(sys.argv) < 3:
        _usage()
        exit(0)
    obj = cli(args[1], args[2])
    if not obj.start():
        print "Failed!!"
