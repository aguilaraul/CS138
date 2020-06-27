#
# author    Raul Aguilar
# date      June 26, 2020
#
# CS 138 1538 Homework 9 Project 2
# Write a modified Button class that creates circular buttons.
#
# Algorithm:
#
from random import randrange
from graphics import GraphWin, Point

from button import Button
from cbutton import CButton
from dieview import DieView

def main():
    # Create the application window
    win = GraphWin("Die Roller")
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")

    # Draw the interface widgets
    die1 = DieView(win, Point(3, 7), 2)
    die2 = DieView(win, Point(7, 7), 2)
    rollButton = CButton(win, Point(2.5, 3), 2, "Roll Dice")
    rollButton.activate()
    quitButton = CButton(win, Point(7.5, 3), 2, "Quit")

    # Event loop
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):
            value1 = randrange(1, 7)
            die1.setValue(value1)
            value2 = randrange(1, 7)
            die2.setValue(value2)
            quitButton.activate()
        pt = win.getMouse()

    # close window
    win.close()

main()