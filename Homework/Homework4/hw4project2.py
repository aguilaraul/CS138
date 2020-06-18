#
# author    Raul Aguilar
# date      June 15, 2020
# CS 138 1535 Homework 4 Project 2
# This program allows the user to draw a line segment and then displays some
# graphical and textual information about the line segment.
#
from graphics import *
import math

def main():
    win = GraphWin("Line!")
    
    # Get the two points
    print("Set the start of the line")
    p1 = win.getMouse()
    p1.draw(win)
    print("You clicked at:", p1.getX(), p1.getY())

    print("Set the end of the line")
    p2 = win.getMouse()
    print("You clicked at:", p2.getX(), p2.getY())

    # Draw the line on screen
    Line(p1, p2).draw(win)

    # Draw midpoint in cyan
    midpoint = Point((p1.getX()+p2.getX())/2, (p1.getY()+p2.getY())/2)
    midpoint.setFill("cyan")
    midpoint.draw(win)

    # Calculate
    dx = p2.getX() - p1.getX()
    dy = p2.getY() - p1.getY()
    slope  = dy/dx
    length = math.sqrt(dx**2+dy**2)

    print("Slope:", slope)
    print("Length:", length)
    win.getMouse()


main()