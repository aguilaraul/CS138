#
# author    Raul Aguilar
# date      June 29, 2020
#
# CS 138 1535 Homework 10 Project 2
# Create a GUI with a text box, button and a picture. The user will
# type in the suit of a card (spade, clubs, hearts, diamond) and it
# will show the corresponding suit. Use a dictionary as the storage
# mechanism.
#
# Algorithm:
# 1. Populate suit dictionary with matching unicode
# 2. Draw GUI (prompt, textbox, where suit is gonna be, and buttons)
# 3. Ask user to enter card suit
# 4. Turn it into lowercase
# 5. Check to see if it's in the dictionary
#     if it is, draw the suit
#     if not, say invalid suit
# 6. Wait for another entry until exit
#
from graphics import *
from button import Button

WINW = 640
WINH = 480

def populateSuitDict():
    suits = {"club": "\u2663", "spade":"\u2664",
            "heart":"\u2665", "diamond":"\u2666"}
    return suits

def drawPromptAndEntryBox(win):
    suitPrompt = Text(Point(WINW/3, WINH/5), "Enter the suit of a card:")
    suitPrompt.draw(win)
    suitEntry = Entry(Point(WINW - WINW/3, WINH/5), 15)
    suitEntry.setFill("white")
    suitEntry.draw(win)
    return suitEntry

def main():
    suits = populateSuitDict()
    win = GraphWin("Pick a suit, any suit", WINW, WINH)
    
    # Draw prompt and textbox
    suitEntry = drawPromptAndEntryBox(win)

    # Secretly draw where suit is going to be
    suitImg = Text(Point(WINW/2, WINH/2), "")
    suitImg.draw(win)

    # Draw buttons
    drawButton = Button(win, Point(WINW/3, WINH-WINH/5), 150, 40, "Draw Suit")
    drawButton.activate()
    quitButton = Button(win, Point(WINW - WINW/3, WINH-WINH/5), 150, 40, "Quit")
    quitButton.activate()

    # action listener
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if drawButton.clicked(pt):
            validSuit = True
            suit = suitEntry.getText().lower()

            if suit in suits:
                suitCode = suits[suit]
            else:
                validSuit = False

            if validSuit:
                suitImg.setSize(36)
                suitImg.setText(suitCode)
            else:
                suitImg.setSize(12)
                suitImg.setText("Invalid entry.")
        pt = win.getMouse()

main()