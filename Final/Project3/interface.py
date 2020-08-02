# interface.py
#
# author    Raul Aguilar
# date      August 1, 2020
#
# CS 138 1535 Final Project 3
#
#
from graphics import *
from button import Button

WINW = 960
WINH = 640

class Interface:
    def __init__(self):
        self.win = GraphWin("Employee Database", WINW, WINH)
        banner = Text(Point(WINW/2, WINH/16), "Employee Database")
        banner.setSize(24)
        banner.setStyle("bold")
        banner.draw(self.win)
        self.buttons = []
        self.entries = []
        self.texts = []
        self.draw_main_menu()


    def close(self):
        self.win.close()

    def choose(self, choices):
        buttons = self.buttons

        for b in buttons:
            if b.getLabel() in choices:
                b.activate()
            else:
                b.deactivate()

        while True:
            p = self.win.getMouse()
            for b in buttons:
                if b.clicked(p):
                    return b.getLabel()

    def draw_main_menu(self):
        buttons = self.buttons
        b = Button(self.win, Point(WINW/6, WINH-WINH/16), 140, 30, "Add Employee")
        buttons.append(b)
        b = Button(self.win, Point((WINW/6)*2, WINH-WINH/16), 140, 30, "Remove Employee")
        buttons.append(b)
        b = Button(self.win, Point((WINW/6)*3, WINH-WINH/16), 140, 30, "Save Database")
        buttons.append(b)
        b = Button(self.win, Point((WINW/6)*4, WINH-WINH/16), 140, 30, "Load Database")
        buttons.append(b)
        b = Button(self.win, Point((WINW/6)*5, WINH-WINH/16), 75, 30, "Exit")
        buttons.append(b)

    def undraw_main_menu(self):
        for b in self.buttons:
            b.undraw()
        self.buttons.clear()

    def draw_add_employee(self):
        buttons = self.buttons
        # Type of Employee
        b = Button(self.win, Point(WINW/5, WINH/3), 150, 30, "Parttime Employee")
        buttons.append(b)
        b = Button(self.win, Point(WINW/5, (WINH/3)*1.5), 150, 30, "Salary Employee")
        buttons.append(b)
        b = Button(self.win, Point(WINW / 5, (WINH / 3) * 2), 150, 30, "Hourly Employee")
        buttons.append(b)

        # Exit & Back
        b = Button(self.win, Point((WINW / 6)*4, WINH - WINH / 16), 75, 30, "Back")
        buttons.append(b)
        b = Button(self.win, Point((WINW/6)*5, WINH-WINH/16), 75, 30, "Exit")
        buttons.append(b)
    
    def undraw_add_employee(self):
        for b in self.buttons:
            b.undraw()
        self.buttons.clear()
    
    def draw_add_parttime(self):
        buttons = self.buttons
        b = Button(self.win, Point(WINW/5, WINH-WINH/16), 150, 30, "Add Employee")
        buttons.append(b)

    def main_menu(self):
        while True:
            ans = self.choose(["Add Employee", "Remove Employee", "Save Database", "Load Database", "Exit"])

            if ans == "Add Employee":
                self.add_employee()

    def add_employee(self):
        self.undraw_main_menu()
        self.draw_add_employee()

        while True:
            ans = self.choose(["Back", "Exit", "Parttime Employee", "Salary Employee", "Hourly Employee"])
            break

        if ans == "Back":
            self.undraw_add_employee()
            return self.draw_main_menu()