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
    win = GraphWin("Line!", 300, 300)
    
    # Get the two points
    message = Text(Point(150, 280), "Set the start of the line")
    message.draw(win)
    print("Set the start of the line")
    
    # draw the first point
    p1 = win.getMouse()
    p1.draw(win)

    message.setText("You clicked at: {}, {}".format(p1.getX(), p1.getY()))
    print("You clicked at:", p1.getX(), p1.getY())

    # get the second point
    message2 = Text(Point(150, 295), "Set the end of the line")
    message2.draw(win)
    print("Set the end of the line")
    
    p2 = win.getMouse()
    
    message.setText("You clicked at: {}, {}".format(p2.getX(), p2.getY()))
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
    
    # click again before exit
    message2.setText("Click anywhere to exit")
    win.getMouse()
    win.close()


main()