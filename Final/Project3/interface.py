# interface.py
#
# author    Raul Aguilar
# date      August 5, 2020
#
# CS 138 1535 Final Project 3
# Graphical interface to interact with the employee database.
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

    # Screens
    def undrawMenu(self):
        for b in self.buttons: b.undraw()
        self.buttons.clear()
        for e in self.entries: e.undraw()
        self.entries.clear()
        for t in self.texts: t.undraw()
        self.texts.clear()

    def drawExitBackButtons(self):
        b = Button(self.win, Point((WINW / 6)*4, WINH - WINH / 16), 75, 30, "Back")
        self.buttons.append(b)
        b = Button(self.win, Point((WINW/6)*5, WINH-WINH/16), 75, 30, "Exit")
        self.buttons.append(b)
    
    def drawMainMenu(self):
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

    def mainMenu(self):
        self.undrawMenu()
        self.drawMainMenu()
        while True:
            ans = self.choose(["Add Employee", "Remove Employee", "Save Database", "Load Database", "Exit"])
            return ans

    # Add Employee Screens
    def drawAddEmployee(self):
        buttons = self.buttons
        # Types of Employee
        b = Button(self.win, Point(WINW/5, WINH/3), 150, 30, "Parttime Employee")
        buttons.append(b)
        b = Button(self.win, Point(WINW/5, (WINH/3)*1.5), 150, 30, "Salary Employee")
        buttons.append(b)
        b = Button(self.win, Point(WINW / 5, (WINH / 3) * 2), 150, 30, "Hourly Employee")
        buttons.append(b)
        # Exit and Back
        self.drawExitBackButtons()

    def addEmployee(self):
        self.undrawMenu()
        self.drawAddEmployee()
        while True:
            ans = self.choose(["Back", "Exit", "Parttime Employee", "Salary Employee", "Hourly Employee"])
            return ans

    def drawTypeEmployee(self, choice):
        self.undrawMenu() # undraw previous menu
        entries = self.entries
        texts = self.texts
        
        # Draw buttons
        b = Button(self.win, Point(WINW/5, WINH-WINH/16), 150, 30, "Add Employee")
        self.buttons.append(b)
        self.drawExitBackButtons()
        
        # Draw Text + Entries
        t = Text(Point(WINW/3, (WINH/16)*3), "First Name:")
        texts.append(t)
        e = Entry(Point((WINW/3)*2, (WINH/16)*3), 20)
        entries.append(e)
        t = Text(Point(WINW/3, (WINH/16)*4), "Last Name:")
        texts.append(t)
        e = Entry(Point((WINW/3)*2, (WINH/16)*4), 20)
        entries.append(e)
        t = Text(Point(WINW/3, (WINH/16)*5), "ID Number:")
        texts.append(t)
        e = Entry(Point((WINW/3)*2, (WINH/16)*5), 20)
        entries.append(e)

        if choice == "Parttime Employee":
            t = Text(Point(WINW/3, (WINH/16)*6), "Amount per class: $")
            texts.append(t)
            e = Entry(Point((WINW/3)*2, (WINH/16)*6), 20)
            entries.append(e)
            t = Text(Point(WINW/3, (WINH/16)*7), "Number of classes teaching:")
            texts.append(t)
            e = Entry(Point((WINW/3)*2, (WINH/16)*7), 20)
            entries.append(e)
        elif choice == "Salary Employee":
            t = Text(Point(WINW/3, (WINH/16)*6), "Salary: $")
            texts.append(t)
            e = Entry(Point((WINW/3)*2, (WINH/16)*6), 20)
            entries.append(e)
        else:
            t = Text(Point(WINW/3, (WINH/16)*6), "Hourly rate: $")
            texts.append(t)
            e = Entry(Point((WINW/3)*2, (WINH/16)*6), 20)
            entries.append(e)
            t = Text(Point(WINW/3, (WINH/16)*7), "Hours worked:")
            texts.append(t)
            e = Entry(Point((WINW/3)*2, (WINH/16)*7), 20)
            entries.append(e)

        for e in entries:
            e.setFill("white")
            e.draw(self.win)
        for t in texts:
            t.setStyle("bold")
            t.draw(self.win)

    def addTypeEmployee(self, choice):
        self.drawTypeEmployee(choice)
        while True:
            ans = self.choose(["Back", "Exit", "Add Employee"])
            return ans

    # Remove Employee Screens
    def drawRemoveEmployee(self):
        self.undrawMenu() # undraw previous menu
        entries = self.entries
        texts = self.texts
        b = Button(self.win, Point(WINW/5, WINH-WINH/16), 150, 30, "Remove Employee")
        self.buttons.append(b)
        self.drawExitBackButtons()
        t = Text(Point(WINW/3, (WINH/16)*3), "Employee ID:")
        texts.append(t)
        e = Entry(Point((WINW/3)*2, (WINH/16)*3), 20)
        entries.append(e)

        for t in texts:
            t.setStyle("bold")
            t.draw(self.win)
        for e in entries:
            e.setFill("white")
            e.draw(self.win)

    def removeEmployee(self):
        self.drawRemoveEmployee()

        while True:
            ans = self.choose(["Back", "Exit", "Remove Employee"])
            return ans