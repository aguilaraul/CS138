# interface.py
#
# author    Raul Aguilar
# date      July 27, 2020
#
# CS 138 1535 Final Project 1
# Graphical Interface for the spell checker. Displays a window with
# text, two entries, and a spell check button.
#
from graphics import *
from button import Button

WINW = 320
WINH = 120


class Interface:
    def __init__(self):
        self.win = GraphWin("Spell Checker", WINW, WINH)
        self.win.setBackground("lightyellow")
        self.buttons = []
        self.entries = []
        self.texts = []

        # Draw text
        t = Text(Point(WINW/5, WINH/3), "Dictionary:")
        self.texts.append(t)
        t = Text(Point(WINW/5, WINH/3+20), "File:")
        self.texts.append(t)

        for t in self.texts:
            t.setStyle("bold")
            t.draw(self.win)

        # Draw entry boxes
        e = Entry(Point(WINW-WINW/3, WINH/3), 20)
        self.entries.append(e)
        e = Entry(Point(WINW-WINW/3, WINH/3+20), 20)
        self.entries.append(e)

        for e in self.entries:
            e.setFill("pink")
            e.setFace("courier")
            e.draw(self.win)

        # Draw 'Spell Check' button
        b = Button(self.win, Point(WINW-WINW/6, WINH-20), 100, 30, "Spell Check")
        b.rect.setFill("lightblue")
        self.buttons.append(b)

    def close(self):
        self.win.close()

    def choose(self, choices):
        buttons = self.buttons

        # activate choice buttons, deactiave others
        for b in buttons:
            if b.getLabel() in choices:
                b.activate()
            else:
                b.deactivate()

        # get mouse click until an active button is clicked
        while True:
            p = self.win.getMouse()
            for b in buttons:
                if b.clicked(p):
                    return b.getLabel()

    def checkSpelling(self):
        while True:
            ans = self.choose(["Spell Check"])
            return ans == "Spell Check"