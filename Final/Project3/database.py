#
#
#
from parttime_employee import ParttimeEmployee
from salary_employee import SalaryEmployee
from hourly_employee import HourlyEmployee

class Database:
    def __init__(self):
        self.database = dict()
        self.id = 0

    def addEmployee(self):
        type_ = input("Type of employee: ")
        type_ = type_.lower()
        first = input("First name: ")
        last = input("Last name: ")
        id_ = self.id+1
        if type_ == "parttime":
            pay = int(input("Base pay per class: "))
            classes = int(input("Number of classes teaching: "))
            self.database[id_] = ParttimeEmployee(first, last, id_, pay, classes)

        print("{} {} was added to the database.\n".format(first, last))
