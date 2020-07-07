# videopoker.py
from graphics import *
from button import Button
from dieview import DieView

WINW = 600
WINH = 400

class GraphicsInterface:
    def __init__(self):
        self.win = GraphWin("Dice Poker", WINW, WINH)
        self.win.setBackground("green3")
        banner = Text(Point(300, 30), "Python Poker Parlor")
        banner.setSize(24)
        banner.setFill("yellow2")
        banner.setStyle("bold")
        # Draw the splash screen
        banner.draw(self.win)
        self.buttons = []
        b = Button(self.win, Point(WINW/3, WINH-WINH/5), 150, 40, "Let's Play")
        self.buttons.append(b)
        b = Button(self.win, Point(WINW-WINW/3, WINH-WINH/5), 150, 40, "Exit")
        self.buttons.append(b)
        self.rules = []
        self.displayRules()

    def displayRules(self):
        """Draws the rules of the game on the splash screen as part of
        the initialization."""
        text = ["You start with $100",
                "Each round costs $10 to play",
                "You start with a random hand and get two chances to reroll",
                "At the end of the hand, you get a payout or nothing",
                "Are you ready to roll?"]
        offset = 0

        for rule in text:
            r = Text(Point(WINW/2, WINH/5+offset), rule)
            r.draw(self.win)
            self.rules.append(r)
            offset += 20

    def displayGame(self):
        """Draws the game's main interface. Should only be drawn after
        the user selects 'Let's Play' from the splash screen."""
        self.msg = Text(Point(300, 380), "Welcome to the Dice Table")
        self.msg.setSize(18)
        self.msg.draw(self.win)
        self.createDice(Point(300, 100), 75)
        self.addDiceButtons(Point(300, 170), 75, 30)
        b = Button(self.win, Point(300, 230), 400, 40, "Roll Dice")
        self.buttons.append(b)
        b = Button(self.win, Point(300, 280), 150, 40, "Score")
        self.buttons.append(b)
        b = Button(self.win, Point(570, 375), 40, 30, "Quit")
        self.buttons.append(b)
        b = Button(self.win, Point(30, 375), 40, 30, "Help")
        self.buttons.append(b)
        self.money = Text(Point(300, 325), "$100")
        self.money.setSize(18)
        self.money.draw(self.win)

    def createDice(self, center, size):
        center.move(-3 * size, 0)
        self.dice = []
        for i in range(5):
            view = DieView(self.win, center, size)
            self.dice.append(view)
            center.move(1.5 * size, 0)

    def addDiceButtons(self, center, width, height):
        center.move(-3 * width, 0)
        for i in range(1, 6):
            label = "Die {0}".format(i)
            b = Button(self.win, center, width, height, label)
            self.buttons.append(b)
            center.move(1.5 * width, 0)

    def setMoney(self, amt):
        self.money.setText("${0}".format(amt))

    def showResult(self, msg, score):
        if score > 0:
            text = "{0}! You win ${1}".format(msg, score)
        else:
            text = "You rolled {0}".format(msg)
        self.msg.setText(text)

    def setDice(self, values):
        for i in range(5):
            self.dice[i].setValue(values[i])

    def choose(self, choices):
        buttons = self.buttons

        # activate choice buttons, deactivate others
        for b in buttons:
            if b.getLabel() in choices:
                b.activate()
            else:
                b.deactivate()

        # get mouse clicks until an active button is clicked
        while True:
            p = self.win.getMouse()
            for b in buttons:
                if b.clicked(p):
                    return b.getLabel()  # function exit here

    def splashScreen(self):
        """Interactive buttons on the splash screen before the start of
        the game. If 'Let's Play' is selected, the rules and buttons
        are undrawn and the game interface is drawn before returning
        True to start the game. Otherwise, 'Exit' exits the game."""
        while True:
            ans = self.choose(["Let's Play", "Exit"])

            if ans == "Let's Play":
                # Undraw the rules and buttons
                for rule in self.rules:
                    rule.undraw()
                for button in self.buttons:
                    button.undraw()
                self.buttons.clear() # clear out the buttons
                # Draw the game interface
                self.displayGame()
                return True
            else:
                return False

    def wantToPlay(self):
        while True:
            ans = self.choose(["Roll Dice", "Quit", "Help"])
            if ans == "Help":
                self.winHelp()
            else:
                self.msg.setText("")
                return ans == "Roll Dice"

    def chooseDice(self):
        # Choices is a list of indexes of the selected dice
        choices = []
        while True:
            # Wait for user to click a valid button
            b = self.choose(["Die 1", "Die 2", "Die 3", "Die 4", "Die 5",
                             "Roll Dice", "Score", "Help"])

            if b[0] == "D":
                i = int(b[4]) - 1
                if i in choices:
                    choices.remove(i)
                    self.dice[i].setColor("black")
                else:
                    choices.append(i)
                    self.dice[i].setColor("gray")
            else:
                for d in self.dice:
                    d.setColor("black")
                if b == "Score":
                    return []
                if b == "Help":
                    self.winHelp()
                elif choices != []:
                    return choices

    def close(self):
        self.win.close()

    def winHelp(self):
        """Displays the help window. Contains the score payouts of each
        winning hand."""
        helpWin = GraphWin("Help: Score Payout", 400, 200)
        backdrop = Rectangle(Point(10, 10), Point(390, 190))
        backdrop.setFill("lightgrey")
        backdrop.setOutline("green3")
        backdrop.draw(helpWin)
        helpWin.setBackground("green3")

        titles = "{} {:>75}".format("Hand", "Pay")
        title = Text(Point(400/2, 20), titles)
        title.draw(helpWin)
        Line(Point(10, 30), Point(390, 30)).draw(helpWin)
        p = Text(Point(400/2, 45), "{:<20} {:>60}".format("Two Pairs", "5"))
        p.draw(helpWin)
        p = Text(Point(400/2, 65), "{:<17} {:>60}".format("Three of a Kind", "8"))
        p.draw(helpWin)
        p = Text(Point(400/2, 85), "{:<18} {:>61}".format("Full House", "12"))
        p.draw(helpWin)
        p = Text(Point(400/2, 105), "{:<12} {:>63}".format("Four of a Kind", "15"))
        p.draw(helpWin)
        p = Text(Point(400/2, 125), "{:<21} {:>61}".format("Straight", "20"))
        p.draw(helpWin)
        p = Text(Point(400/2, 145), "{:<17} {:>60}".format("Five of a Kind", "30"))
        p.draw(helpWin)