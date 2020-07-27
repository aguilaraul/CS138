# spellchecker.py
#
# author    Raul Aguilar
# date      July 27, 2020
#
# CS 138 1535 Final Project 1
#
#
from string import punctuation

class SpellChecker():
    def __init__(self, filename):
        self.dictionary = self.populateDictionary(filename)

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