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
        #if choice == "Add Employee":
            #self.interface.add_employee()

        #else:
            #self.interface.close()