# salary_employee.py
#
# author    Raul Aguilar
# date      July 27, 2020
#
# CS 138 1535 Final Project 3
# One of three employee types. The salary emplyoee is a paid a monthly
# salary.
#
from employee import Employee


class SalaryEmployee(Employee):
    def __init__(self, first, last, id, salary):
        super().__init__(first, last, id)
        self.salary = salary

    def getSalary(self):
        return self.salary

    def calculate_pay(self):
        return self.salary