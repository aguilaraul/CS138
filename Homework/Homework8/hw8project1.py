#
# author    Raul Aguilar
# date      June 24, 2020
#
# CS 138 1535 Homework 8 Project 1
# Write a program that converts a color image to grayscale.
#
# Algorithm
# 1. Ask for the image file name
# 2. Ask for save file name
# 3. Get image width and height
# 4. Set row and column to 0,0
# 5. for each row in the width:
#   for each column in the height:
#        r, g, b = get pixel information for current row and column
#        brightness = int(round(0.299r + 0.587g + 0.114b))
#        set pixel color to color_rgb(brightness, brightness, brightness)
#    update the image to see progress row by row
# 6. Save image file and exit
#
from graphics import *

def main():
    winWidth = 640
    winHeight = 480
    infile = input("Enter the file name:")
    outfile = input("Enter the name of save file:")

    # Open window and image
    win = GraphWin("Grayscale Converter", winWidth, winHeight)
    img = Image(Point(winWidth/2, winHeight/2), infile)
    imgWidth = img.getWidth()
    imgHeight = img.getHeight()
    img.draw(win)

    # Converting to grayscale
    row = 0
    column = 0

    for row in range(imgWidth):
        for column in range(imgHeight):
            r, g, b = img.getPixel(row, column)
            brightness = int(round((0.299*r) + (0.587*g) + (0.114*b)))
            img.setPixel(row, column, color_rgb(brightness, brightness, brightness))
            win.update()

    # Save image
    img.save(outfile)
    print("\nConversion complete and saved to", outfile)
    print("\nClick anywhere to exit.")

    # Click to exit
    win.getMouse()
    win.close()

main()