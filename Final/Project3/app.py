# app.py
#
# author    Raul Aguilar
# date      August 5, 2020
#
# CS 138 1535 Final Project 3
#
#
from tkinter.filedialog import askopenfilename, asksaveasfilename

class App:
    def __init__(self, inter, database):
        self.interface = inter
        self.database = database

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

    def addEmployee(self):
        choice = self.interface.addEmployee()

        if choice == "Exit":
            return self.interface.close()
        elif choice == "Back":
            return self.mainMenu()
        else:
            return self.addTypeEmployee(choice)

    def addTypeEmployee(self, employeeType):
        choice = self.interface.addTypeEmployee(employeeType)

        if choice == "Exit":
            return self.interface.close()
        elif choice == "Back":
            return self.addEmployee()
        else:
            self.database.addEmployee(employeeType)
            return self.addEmployee()

    def removeEmployee(self):
        choice = self.interface.removeEmployee()
        
        if choice == "Exit":
            return self.interface.close()
        elif choice == "Back":
            return self.mainMenu()
        else:
            self.database.removeEmployee()
            return self.mainMenu()

    def saveDatabase(self):
        filepath = asksaveasfilename()
        if filepath != "":
            savefile = open(filepath, "w")
            self.database.saveDatabase(savefile)
        return self.mainMenu()