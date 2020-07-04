#
# author    Raul Aguilar
# date      June 29, 2020
#
# CS 138 1535 Homework 10 Extra Credit
# Modify Homework 10 Project 2 to show a complete deck of cards
#
# Algorithm:
# 1. Populate lists for suit and ranks
# 2. Draw window
# 3. Draw entry boxes for color, rank, and suit
# 4. Secretly draw where the card is going to be
# 5. Draw the buttons
# 6. Ask user to enter rank and suit, color is optional
# 7. Validate rank
# 8. Validate suit
# 9. If valid rank and suit, draw the card
# 10. If not valid rank and suit, say invalid entries
# 11. Wait for next entry until exit
#
from graphics import *
from button import Button

WINW = 640
WINH = 480

def populateSuitDict():
    suits = {"club": "\u2663", "spade":"\u2664",
            "heart":"\u2665", "diamond":"\u2666"}
    return suits

def drawEntryBoxes(win):
    colorPrompt = Text(Point(WINW/3, WINH/5-50), "Enter a color:")
    colorPrompt.draw(win)
    colorEntry = Entry(Point(WINW-WINW/3, WINH/5-50), 15)
    colorEntry.setFill("white")
    colorEntry.draw(win)

    rankPrompt = Text(Point(WINW/3, WINH/5-25), "Enter the rank of the card:")
    rankPrompt.draw(win)
    rankEntry = Entry(Point(WINW - WINW/3, WINH/5-25), 15)
    rankEntry.setFill("white")
    rankEntry.draw(win)

    suitPrompt = Text(Point(WINW/3, WINH/5), "Enter the suit of a card:")
    suitPrompt.draw(win)
    suitEntry = Entry(Point(WINW - WINW/3, WINH/5), 15)
    suitEntry.setFill("white")
    suitEntry.draw(win)
    return colorEntry, rankEntry, suitEntry

def main():
    suits = populateSuitDict()
    ranks = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "JACK", "QUEEN", "KING", "ACE"]
    win = GraphWin("Pick a card, any card", WINW, WINH)

    # Draw text entries
    colorEntry, rankEntry, suitEntry = drawEntryBoxes(win)

    # Secretly draw where the card is going to be
    suitImg = Text(Point(WINW/2, WINH/2), "")
    suitImg.draw(win)
    
    rankImg = Text(Point(WINW/2-50, WINH/2-70), "")
    rankImg.draw(win)

    frame = Rectangle(Point(WINW/2-60, WINH/2-80), Point(WINW/2+60, WINH/2+80))

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
            validRank = True

            # get color, suit, and rank from Entry boxes
            # color doesn't need to be set, but if it is - it needs to be correct
            color = colorEntry.getText().lower()
            if color == "":
                color = "black"
            rank = rankEntry.getText().upper()
            suit = suitEntry.getText().lower()

            # check if the rank is in the list
            # if so, take the first letter/number
            # if not, set flag to false
            if rank in ranks:
                cardRank = rank[0]
            else:
                validRank = False

            # check if suit is in dictionary
            # if so, retreive unicode for suit
            # if not, set flag to false
            if suit in suits:
                cardSuit = suits[suit]
            else:
                validSuit = False

            if validSuit and validRank:
                suitImg.setSize(36)
                suitImg.setText(cardSuit)
                suitImg.setTextColor(color)
                rankImg.setText(cardRank)
                rankImg.setTextColor(color)
                frame.undraw()
                frame.draw(win)
            else:
                suitImg.setSize(12)
                suitImg.setText("Invalid entry.")
                rankImg.setText("")
        pt = win.getMouse()


main()