#
#
#
from interface import Interface
from database import Database
from app import App

def main():
    inter = Interface()
    db = Database()
    app = App(inter)
    app.mainMenu()

main()