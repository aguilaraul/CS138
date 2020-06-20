#! /usr/bin/python
# File Name:     hw4project1.py
# Programmer:    Raul Aguilar
# Date:          June 20, 2020
# 
# CS 138 1535 Homework 4 Project 1
# Draw a simple picture with at least 3 graphical objects.
#
# Algorithm:
# 1. Draw window
# 2. Draw head
# 3. Draw right eye and clone for left eye
# 4. Draw right pupil and clone for the left
# 5. Draw triangle for mouth
#
from graphics import *

def main():
    win = GraphWin("Picture a smile", 200, 200)

    # draw head
    head = Circle(Point(100, 80), 50)
    head.draw(win)

    # draw eyes
    rightEye = Oval(Point(110, 50), Point(130, 80))
    rightEye.draw(win)

    leftEye = rightEye.clone()
    leftEye.move(-35, 0)
    leftEye.draw(win)

    # draw pupils
    rightPupil = Oval(Point(115, 65), Point(125, 80))
    rightPupil.setFill("black")
    rightPupil.draw(win)

    leftPupil = rightPupil.clone()
    leftPupil.move(-35, 0)
    leftPupil.draw(win)

    # draw mouth
    p1 = Point(80, 95)
    p2 = Point(126, 95)
    p3 = Point(103, 115)
    mouth = Polygon(p3, p1, p2)
    mouth.draw(win)

    # click again before exit
    win.getMouse()
    win.close()

main()