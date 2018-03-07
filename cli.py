"""
cli.py: Opens up a Cli for the user and process the commands
Author: Rahul Radhakrishnan
Email: rahulrad@usc.edu
"""

# !/usr/bin/python

import helper


class Cli:
    company_id = ""

    def show(self):
        print "Usage\n" \
              "-----\n" \
              "help - Displays this menu\n" \
              "done - Exit the Cli!\n" \
              "listall [export path] - List all the employee details and exports(optional) as a csv\n" \
              "search {(str)} [export path] - Search for a string and exports(optional) as a csv\n"

    def listAll(self, export=None):
        helper.getAllEmployeeDetails(self.company_id, export)

    def search(self, search_str, export=None):
        helper.getEmployeeDetails(self.company_id, search_str, export)

    def runCli(self):
        self.company_id = helper.getCompanyId()
        self.show()
        while True:
            user_input = raw_input("Cli> ")
            user_input = user_input.lower().strip().split(' ')

            if user_input[0] == "done":
                break
            if user_input[0] == "help":
                self.show()
            elif user_input[0] == "listall":
                if len(user_input) > 2:
                    self.show()
                elif len(user_input) == 2:
                    self.listAll(user_input[1])
                else:
                    self.listAll()
            elif user_input[0] == "search":
                if len(user_input) > 3 or len(user_input) < 2:
                    self.show()
                elif len(user_input) == 2:
                    self.search(user_input[1].lower())
                else:
                    self.search(user_input[1].lower(), user_input[2])
            else:
                self.show()


if __name__ == "__main__":
    obj = Cli()
    obj.runCli()
