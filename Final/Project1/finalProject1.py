#
# author    Raul Aguilar
# date      July 26, 2020
#
# CS 138 1535 Final Project 1
#
#
from string import punctuation

def binarySearch(x, L):
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

def populateDictionary(filename):
    words = []
    dictionary = open(filename, "r")
    for word in dictionary:
        words.append(word.strip())
    return words


def spellCheck(word, dictionary):
    if len(word) == 0:
        return True

    if word[0] in punctuation:
        return spellCheck(word[1:], dictionary)
    if word[-1] in punctuation:
        return spellCheck(word[:-1], dictionary)

    if binarySearch(word, dictionary) != -1:
        return True
    else:
        return word


def main():
    dictionary = populateDictionary("english.txt")
    book = open("taleoftwocities.txt", "r", encoding='utf-8')

    for line in book:
        if line.strip() != "":
            line_words = line.split()
            for word in line_words:
                #word = word.lower()
                if spellCheck(word, dictionary) != True:
                    print(spellCheck(word, dictionary))

main()