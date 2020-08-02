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

    def run(self):
        self.main_menu()

    def main_menu(self):
        choice = self.interface.main_menu()
        if choice == "Add Employee":
            self.interface.menu()
            self.add_employee(self.interface.add_employee())
        elif choice == "Remove Employee":
            print("Removing Employee")
        elif choice == "Save Database":
            print("Saving database")
        elif choice == "Load Database":
            print("Let's load that database")
        else:
            self.interface.close()

    def add_employee(self, choice):
        if choice == "Back":
            self.interface.menu()
            return self.main_menu()
        if choice == "Exit":
            self.interface.close()