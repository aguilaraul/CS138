#
# author    Raul Aguilar
# date      June 16, 2020
# CS 138 1535 Homework 4 Project 1
# Draw a simple picture with at least 3 graphical objects.
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