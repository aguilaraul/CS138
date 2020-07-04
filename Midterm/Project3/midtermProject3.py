#
# author    Raul Aguilar
# date      July 3, 2020
#
# CS 138 1535 Midterm Project 3
#
# Algorithm:
#
from graphics import *
from cbutton import CButton

def choose(win, choices):
    buttons = choices

    # activate choice buttons, deactivate others
    for b in buttons:
        if b.getLabel() in choices:
            b.activate()
        else:
            b.deactivate()

    # get mouse clicks until an active button is clicked
    while True:
        p = win.getMouse()
        for b in buttons:
            if b.clicked(p):
                return b.getLabel()  # function exit here

def main():
    win = GraphWin("Connect-the-Dots", 600, 600)

    dots = []
    dot = CButton(win, Point(230, 300), 5, "1")
    dots.append(dot)

    while True:
        b = choose(win, dots)

        if b == "1":
            win.setBackground("pink2")

    win.getMouse()


main()