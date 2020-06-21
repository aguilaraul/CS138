#! /usr/bin/python
# File Name:     hw6extraCredit.py
# Programmer:    Raul Aguilar
# Date:          June 20, 2020
#
# CS 138 1535 Homework 6 Extra Credit
# Write a program that draws a circle and then allows the user to click
# the window 10 times.  Each time the user clicks, the circle is moved
# where the user clicked.
#
# Algorithm:
# 1. Draw window and circle
# 2. Display message to move the circle
# 3. User clicks to move circle 10 times
# 
from graphics import *
import random

def randomColor():
    r, g, b = random.randint(0,255), random.randint(0,255), random.randint(0,255)
    return color_rgb(r,g,b)

def moveTo(shape, newCenter):
    oldCenter = shape.getCenter()
    dx = newCenter.getX()-oldCenter.getX()
    dy = newCenter.getY()-oldCenter.getY()
    shape.move(dx, dy)

def main():
    # draw window and circle
    win = GraphWin("Move the circle", 500, 500)
    circle = Circle(Point(250, 250), 30)
    circle.draw(win)

    # display message
    message = Text(Point(250, 490), "Click anywhere to move the circle.")
    message.draw(win)

    # move the circle 10 times
    for i in range(10):
        newCenter = win.getMouse()
        moveTo(circle, newCenter)
        circle.setOutline(randomColor())
        message.setText("Do it {} more times!".format(9-i))

    # click before exit
    message.setText("Click anywhere to exit.")
    win.getMouse()


main()