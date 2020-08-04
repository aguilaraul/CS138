# app.py
# 
# author    Raul Aguilar
# date      August 1, 2020
#
# CS 138 1535 Final Project 3
#

class App:
    def __init__(self, inter):
        self.interface = inter

    def mainMenu(self):
        choice = self.interface.mainMenu()
    
        if choice == "Add Employee":
            return self.addEmployee()
        elif choice == "Remove Employee":
            return self.removeEmployee()
        elif choice == "Save Database":
            return self.saveDatabase()
        elif choice == "Load Database":
            return self.loadDatabase()
        else:
            return self.interface.close()
            

        print(choice) # @Debug

    def addEmployee(self):
        choice = self.interface.addEmployee()

        if choice == "Exit":
            return self.interface.close()
        elif choice == "Back":
            return self.mainMenu()
        else:
            return self.addTypeEmployee(choice)

    def addTypeEmployee(self, choice):
        choice = self.interface.addTypeEmployee(choice)

        if choice == "Exit":
            return self.interface.close()
        if choice == "Back":
            return self.addEmployee()

        print(choice) # @Debug