#
# author	Raul Aguilar
# date		July 5, 2020
#
# CS 138 1535 Homework 11 Project 2
#
from graphics import *
from button import Button

WINW = 600
WINH = 480

class ATMInterface:
	def __init__(self):
		self.win = GraphWin("Automatic Teller Machine", WINW, WINH)
		self.win.setBackground("grey")
		self.account = []
		self.buttons = []
		self.entries = []
		self.texts = []
		banner = Text(Point(WINW/2, 30), "Bank of Computer Science")
		banner.setSize(24)
		banner.setFill("white")
		banner.setStyle("bold")
		banner.draw(self.win)
		self.drawLoginScreen()


	def drawLoginScreen(self):
		self.balance = Text(Point(0,0), "")
		self.loginmsg = Text(Point(WINW/2, WINH-WINH/3), "")
		self.texts.append(self.loginmsg)

		# Entry Boxes
		t = Text(Point(WINW/3, WINH/3), "Username")
		self.texts.append(t)
		t = Text(Point(WINW/3, WINH/3+30), "Password")
		self.texts.append(t)

		e = Entry(Point(WINW-WINW/3, WINH/3), 20)		# username entry
		self.entries.append(e)
		e = Entry(Point(WINW-WINW/3, WINH/3+30), 20)	# password entry
		self.entries.append(e)

		for t in self.texts:
			t.setTextColor("white")
			t.setStyle("bold")
			t.setFace("courier")
			t.draw(self.win)

		for e in self.entries:
			e.setFace("courier")
			e.setFill("lightgrey")
			e.draw(self.win)

		# Login Buttons
		b = Button(self.win, Point(WINW/3, WINH-WINH/5), 150, 40, "Login")
		self.buttons.append(b)
		b = Button(self.win, Point(WINW-WINW/3, WINH-WINH/5), 150, 40, "Exit")
		self.buttons.append(b)

	
	def undrawLoginScreen(self):
		for t in self.texts:
			t.undraw()
		for e in self.entries:
			e.undraw()
		for b in self.buttons:
			b.undraw()
		
		self.texts.clear()
		self.entries.clear()
		self.buttons.clear()


	def close(self):
		self.win.close()


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
		

	def setLoginMsg(self, text):
		self.loginmsg.setText(text)

	
	def login(self):
		while True:
			ans = self.choose(["Login", "Exit"])
			return ans == "Login"


	def accountView(self, accountDetails):
		self.account = accountDetails
		firstName = self.account[self.account.index("first name")+1]
		money = int(self.account[self.account.index("balance")+1])
		t = Text(Point(100, 100), "Welcome {},".format(firstName))
		self.texts.append(t)
		self.balance = Text(Point(120, 120), "{}: ${}".format("Balance", money))
		self.texts.append(self.balance)

		for t in self.texts:
			t.setFace("courier")
			t.setTextColor("white")
			t.draw(self.win)

		b = Button(self.win, Point(WINW-50, WINH-11), 100, 22, "Logout")
		self.buttons.append(b)

		while True:
			b = self.choose(["Logout"])

			return b == "Logout"

	
	def undrawAccountView(self):
		for t in self.texts:
			t.undraw()
		for b in self.buttons:
			b.undraw()
		self.texts.clear()
		self.buttons.clear()