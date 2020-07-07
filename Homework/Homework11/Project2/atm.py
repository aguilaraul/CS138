import time

class ATM:
    def __init__(self, interface):
        self.acctDetails = []
        self.interface = interface
        self.openAcctDetails()

    def run(self):
        attempts = 0
        if self.interface.login():
            if self.checkLogin():
                self.interface.setLoginMsg("Login successful...")
                time.sleep(2)
                self.interface.undrawLoginScreen()
                if self.interface.accountView(self.acctDetails):
                    self.interface.undrawAccountView()
                    self.interface.drawLoginScreen()
                    self.run()
            else:
                self.interface.setLoginMsg("Wrong username/password")
                self.run()
        self.interface.close()

    def checkLogin(self):
        validUsername = False
        validPassword = False
        credentials = []
        for e in self.interface.entries:
            t = e.getText()
            credentials.append(t)

        usrnme = self.acctDetails[self.acctDetails.index("id")+1]
        psswrd = self.acctDetails[self.acctDetails.index("password")+1]

        validUsername = credentials[0] == usrnme
        validPassword = credentials[1] == psswrd

        return validPassword and validPassword

	
    def openAcctDetails(self):
        filename = "acctdetails.txt"
        infile = open(filename, "r")
        for line in infile:
            a,b = line.split(",")
            self.acctDetails.append(a.strip())
            self.acctDetails.append(b.strip())