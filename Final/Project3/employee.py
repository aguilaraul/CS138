# employee.py
#
# author    Raul Aguilar
# date      July 27, 2020
#
# CS 138 1535 Final Project 3
#

class Employee:
    def __init__(self, first, last, id_):
        self.firstname = first
        self.lastname = last
        self.id_ = id_

    def getFirstName(self):
        return self.firstname
    
    def getLastName(self):
        return self.lastname
    
    def getFullName(self):
        return "{} {}".format(self.firstname, self.lastname)

    def getID(self):
        return self.id_