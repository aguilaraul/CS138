#
# author    Raul Aguilar
# date      June 30, 2020
#
# CS 138 1535 Homework 11 Project 1
#
#
# Algorithm:
#
from pokerapp import PokerApp
from videopoker import GraphicsInterface

def main():
    inter = GraphicsInterface()
    app = PokerApp(inter)
    app.run()

main()