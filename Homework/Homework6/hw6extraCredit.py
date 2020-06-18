#
# author    Raul Aguilar
# date      June 17, 2020
# CS 138 1535 Homework 6 Extra Credit
# Write a program that draws a circle and then allows the user to click
# the window 10 times.  Each time the user clicks, the circle is moved
# where the user clicked.
#
from graphics import *

def moveTo(shape, newCenter):
    oldCenter = shape.getCenter()
    dx = newCenter.getX()-oldCenter.getX()
    dy = newCenter.getY()-oldCenter.getY()
    shape.move(dx, dy)

def main():
    win = GraphWin("Move the circle", 500, 500)
    circle = Circle(Point(250, 250), 30)
    circle.draw(win)

    # display message
    message = Text(Point(250, 490), "Click anywhere to move the circle.")
    message.draw(win)

    for i in range(10):
        newCenter = win.getMouse()
        moveTo(circle, newCenter)
        message.setText("Do it {} more times!".format(9-i))

    # click before exit
    message.setText("Click anywhere to exit.")
    win.getMouse()


main()