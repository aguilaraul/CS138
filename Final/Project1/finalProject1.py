#
# author    Raul Aguilar
# date      July 26, 2020
#
# CS 138 1535 Final Project 1
#
#
from string import punctuation
from interface import Interface
from spellchecker import SpellChecker

def main():
    Interface()
    SpellChecker()

    #dictionary = SpellChecker.populateDictionary("english.txt")
    book = open("taleoftwocities.txt", "r", encoding='utf-8')

    for line in book:
        if line.strip() != "":
            line_words = line.split()
            for word in line_words:
                word = word.lower()
                if SpellChecker.spellCheck(word) != True:
                    print(spellCheck(word))


main()