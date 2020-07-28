# spellchecker.py
#
# author    Raul Aguilar
# date      July 27, 2020
#
# CS 138 1535 Final Project 1
#
#
#
import os.path
from string import punctuation


class SpellChecker():
    def __init__(self, interface):
        self.interface = interface
        self.dictionary = dict()

    def getDictionary(self):
        return self.interface.entries[0].getText()

    def getFile(self):
        return self.interface.entries[1].getText()

    def populateDictionary(self, filename):
        dictionary = []
        words = open(filename, "r")
        for word in words:
            dictionary.append(word.strip())
        return dictionary

    def binarySearch(self, x, L):
        low = 0
        high = len(L)-1

        while low <= high:
            mid = (low+high)//2
            item = L[mid]
            if x == item:
                return mid
            elif x < item:
                high = mid-1
            else:
                low = mid+1

        return -1

    def spellCheck(self, word):
        if len(word) == 0:
            return True

        if word[0] in punctuation:
            return self.spellCheck(word[1:])
        if word[-1] in punctuation:
            return self.spellCheck(word[:-1])

        if self.binarySearch(word, self.dictionary) != -1:
            return True
        else:
            return word

    def run(self):
        if self.interface.checkSpelling():
            self.interface.close()
            if os.path.isfile(self.getDictionary()):
                self.dictionary = self.populateDictionary(self.getDictionary())
                if os.path.isfile(self.getFile()):
                    book = open(self.getFile(), "r", encoding='utf-8')
                    print("Misspelled Words:")
                    for line in book:
                        if line.strip() != "":
                            line_words = line.split()
                            for word in line_words:
                                if self.spellCheck(word) != True:
                                    print(self.spellCheck(word))
                else:
                    print("File not found. Re-run and enter correct file.")
            else:
                print("Dictionary not found. Re-run and enter correct dictionary file.")