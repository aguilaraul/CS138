# hourly_employee.py
#
# author    Raul Aguilar
# date      July 28, 2020
#
# CS 138 1535 Final Project 3
# One of three employee types. The hourly employee is paid based on the
# number of hours worked multiplied by their hourly rate.
#
from employee import Employee


class HourlyEmployee(Employee):
    def __init__(self, first, last, id, rate, hours):
        super().__init__(first, last, id)
        self.hourlyRate = rate
        self.hours = hours

    def getHourlyRate(self):
        return self.hourlyRate

    def getHours(self):
        return self.hours

    def calculate_pay(self):
        return self.hourlyRate * self.hours