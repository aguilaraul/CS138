#
# author    Raul Aguilar
# date      June 26, 2020
#
# CS 138 Homework 9 Project 1
# Use the Button class to create GUI for Homework 7 Project 1
#
# Algorithm:
# 1. Draw GUI
# 2. Ask for inputs
# 3. Retreive inputs from entry boxes and convert to appropriate type
# 4. Estimate adult height
# 5. Display results
# 6. Wait for more inputs or exit
#
from graphics import *
from button import Button

WINWIDTH = 640
WINHEIGHT = 480

def drawGenderPrompt(win):
    genderText = Text(Point(WINWIDTH/3, WINHEIGHT/5-50), "Is the child male or female?")
    genderText.setSize(10)
    genderText.draw(win)
    genderEntryBox = Entry(Point(WINWIDTH-(WINWIDTH/3),WINHEIGHT/5 - 50), 20)
    genderEntryBox.setFill('white')
    genderEntryBox.setText("male or female?")
    genderEntryBox.draw(win)
    return genderEntryBox

def drawMotherPrompt(win):
    motherText = Text(Point(WINWIDTH/3, WINHEIGHT/5 - 25), "Enter the mother's height in inches:")
    motherText.setSize(10)
    motherText.draw(win)
    motherEntryBox = Entry(Point(WINWIDTH-(WINWIDTH/3), WINHEIGHT/5 - 25), 20)
    motherEntryBox.setFill('white')
    motherEntryBox.setText("enter height in inches")
    motherEntryBox.draw(win)
    return motherEntryBox

def drawFatherPrompt(win):
    fatherText = Text(Point(WINWIDTH/3, WINHEIGHT/5), "Enter the father's height in inches:")
    fatherText.setSize(10)
    fatherText.draw(win)
    fatherEntryBox = Entry(Point(WINWIDTH-(WINWIDTH/3), WINHEIGHT/5), 20)
    fatherEntryBox.setFill('white')
    fatherEntryBox.setText("enter height in inches")
    fatherEntryBox.draw(win)
    return fatherEntryBox

def drawTexts(win):
    estimateText1 = Text(Point(WINWIDTH/2, WINHEIGHT/2-30), "")
    estimateText2 = Text(Point(WINWIDTH/2, WINHEIGHT/2), "")
    estimateText1.draw(win)
    estimateText2.draw(win)
    return estimateText1, estimateText2

def main():
    win = GraphWin("Estimate Adult Height", WINWIDTH, WINHEIGHT)
    
    # Gender text and entry
    genderEntry = drawGenderPrompt(win)

    # Mother height entry
    motherEntry = drawMotherPrompt(win)

    # Father height entry
    fatherEntry = drawFatherPrompt(win)

    # draw text
    estimateText1, estimateText2 = drawTexts(win)

    # buttons to compute and quit
    estimateButton = Button(win, Point(WINWIDTH/3, WINHEIGHT-WINHEIGHT/5), 150, 40, "Estimate Height")
    estimateButton.activate()
    quitButton = Button(win, Point(WINWIDTH - WINWIDTH/3, WINHEIGHT-WINHEIGHT/5), 150, 40, "Quit")
    quitButton.activate()

    # Event loop
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if estimateButton.clicked(pt):
            validGenderEntry = False
            validMotherEntry = False
            validFatherEntry = False

            # Validate gender entry
            gender = genderEntry.getText()
            if((gender == "male") or (gender == "female")):
                genderEntry.setTextColor("black")
                validGenderEntry = True
            else:
                genderEntry.setTextColor("red")

            # Validate mother entry
            try:
                motherHeight = float(motherEntry.getText())
                motherEntry.setTextColor("black")
                validMotherEntry = True
            except:
                motherEntry.setTextColor("red")

            # Validate father entry    
            try:
                fatherHeight = float(fatherEntry.getText())
                fatherEntry.setTextColor("black")
                validFatherEntry = True
            except:
                fatherEntry.setTextColor("red")
                
            if(not (validGenderEntry and validMotherEntry and validFatherEntry)):
                estimateText1.setText("Invalid entries")
                estimateText2.setText("")
            else:
                if(gender == "male"):
                    childHeight = ((motherHeight*13/12)+fatherHeight)/2
                else:
                    childHeight = ((fatherHeight*12/13)+motherHeight)/2
                
                feet = int(childHeight//12)
                inches = int(childHeight%12)

                inchesStr = "The estimated height as an adult is {:.2f} inches".format(childHeight)
                feetInchesStr = "{} feet {} inches".format(feet, inches)
                estimateText1.setText(inchesStr)
                estimateText2.setText(feetInchesStr)

        pt = win.getMouse()

    # Click before exit
    win.close()

main()
