#
# author    Raul Aguilar
# date      July 27, 2020
#
# CS 138 1535 Final Project 1
#
#
#
from interface import Interface
from spellchecker import SpellChecker

def main():
    inter = Interface()
    sc = SpellChecker(inter)
    sc.run()
    input("Press Return to exit.")


main()