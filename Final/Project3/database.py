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

        print("{}: {} was removed from the database.\n".format(employee.getID(), employee.getFullName()))

    def saveDatabase(self, savefile):
        for employee in self.database.values():
            print("First name: {}".format(employee.getFirstName()), file=savefile)
            print("Last name: {}".format(employee.getLastName()), file=savefile)
            savefile.write("ID: {}\n".format(employee.getID()))
            if isinstance(employee, ParttimeEmployee):
                savefile.write("Parttime Employee\n")
                savefile.write("Base pay: {}\n".format(employee.getBasePay()))
                savefile.write("Classes: {}\n".format(employee.getClasses()))
            elif isinstance(employee, SalaryEmployee):
                savefile.write("Salary Employee\n")
                savefile.write("Salary: {}\n".format(employee.getSalary()))
            else:
                savefile.write("Hourly Employee\n")
                savefile.write("Hourly rate: {}\n".format(employee.getHourlyRate()))
                savefile.write("Hours worked: {}\n".format(employee.getHours()))

        savefile.close()
        print("Database saved.")

    def loadDatabase(self, loadfile):
        employees = loadfile.readlines()

        count = 1
        for line in employees:
            if count < 4:
                print(line.strip())

            if count == 4:
                type_ = line.strip()
                if type_ == "Parttime Employee":


            count += 1
