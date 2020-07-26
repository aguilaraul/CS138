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

def main():
    dictionary = populateDictionary("english_win.txt")

    book = open("prideandprejudice.txt", "r", encoding='utf-8')

    for line in book:
        if line.strip() != "":
            line_words = line.split()
            for word in line_words:
                word = word.lower()
                #for ch in word:
                ch = word[-1]
                if ch in punctuation:
                    #print(word)
                    #print("-->", ch)
                    word = word[:-1]

                #print("New word:", word)
                if binarySearch(word, dictionary) == -1:
                    print("Spell check error:", word)

        #print(line.split())

    #word = input("Enter a word to spell check: ")

    #print(binarySearch(word, words))

main()