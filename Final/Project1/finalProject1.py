#
# author    Raul Aguilar
# date      July 27, 2020
#
# CS 138 1535 Final Project 1
#
#
#
from spellchecker import SpellChecker

def main():
    sc = SpellChecker("english.txt")
    book = open("taleoftwocities.txt", "r", encoding='utf-8')

    for line in book:
        if line.strip() != "":
            line_words = line.split()
            for word in line_words:
                if sc.spellCheck(word) != True:
                    print(sc.spellCheck(word))


main()