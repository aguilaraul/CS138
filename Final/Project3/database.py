# database.py
#
# author    Raul Aguilar
# date      August 5, 2020
#
# CS 138 1535 Final Project 3
# Employee database
#
from parttime_employee import ParttimeEmployee
from salary_employee import SalaryEmployee
from hourly_employee import HourlyEmployee

class Database:
    def __init__(self, interface):
        self.interface = interface
        self.database = dict()

    def addEmployee(self, employeeType):
        interface = self.interface
        first = interface.entries[0].getText()
        last = interface.entries[1].getText()
        id_ = interface.entries[2].getText()
        pay = interface.entries[3].getText()
        if employeeType == "Salary Employee":
            self.database[id_] = SalaryEmployee(first, last, id_, pay)
        else:
            amount = interface.entries[4].getText()
            if employeeType == "Parttime Employee":
                self.database[id_] = ParttimeEmployee(first, last, id_, pay, amount)
            else:
                self.database[id_] = HourlyEmployee(first, last, id_, pay, amount)

        print("{} {} was added to the database.\n".format(first, last))

    def removeEmployee(self):
        id_ = self.interface.entries[0].getText()
        employee = self.database.pop(id_)

        print("{}: {} was removed from the database.\n".format(employee.getID, employee.getFullName()))

    def saveDatabase(self, savefile):
        for employee in self.database.values():
            savefile.write("{}\n".format(employee.getFullName()))
            savefile.write("{}\n".format(employee.getID()))
            if isinstance(employee, ParttimeEmployee):
                print("Parttime Employee", file=savefile)
                print("Base pay: {}".format(employee.getBasePay()), file=savefile)
            elif isinstance(employee, SalaryEmployee):
                print("Salary Employee", file=savefile)
                print("")

        print("Database saved.")
        savefile.close()