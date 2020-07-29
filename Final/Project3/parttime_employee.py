# parttimeemployee.py
#
# author    Raul Aguilar
# date      July 27, 2020
#
# CS 138 1535 Final Project 3
# One of three employee types. The parttime faculty member is paid a
# set amount for each class they teach.
#
from employee import Employee

class ParttimeEmployee(Employee):
    def __init__(self, first, last, id, pay, classes):
        super().__init__(first, last, id)
        self.base_pay = pay
        self.classes = classes

    def calculate_pay(self):
        return self.base_pay * self.classes