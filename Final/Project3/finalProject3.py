# finalProject3.py
#
# author    Raul Aguilar
# date      August 5, 2020
#
# CS 138 1535 Final Project 3
#
#
from interface import Interface
from database import Database
from app import App


def main():
    inter = Interface()
    db = Database(inter)
    app = App(inter, db)
    app.mainMenu()


main()
