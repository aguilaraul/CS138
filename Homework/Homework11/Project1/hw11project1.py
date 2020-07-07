#
# author    Raul Aguilar
# date      July 4, 2020
#
# CS 138 1535 Homework 11 Project 1
# Modify the Dice Poker Program to include a splash screen and a help
# window
#

from pokerapp import PokerApp
from videopoker import GraphicsInterface

def main():
    inter = GraphicsInterface()
    app = PokerApp(inter)
    app.run()

main()