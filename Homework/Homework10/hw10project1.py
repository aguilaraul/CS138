# author    Raul Aguilar
# date      June 29, 2020
#
# CS 138 1535 Homework 10 Project 1
# Create a program that counts the reserved words in a python file.
#
# Algorithm:
# 1. Populate reserved word dictionary with default 0 values
# 2. Ask the user to enter name of python file
# 3. Open Python file
# 4. For each line in the file, strip it of whitespace
# 5. If the line is empty, a comment, or a print statement - ignore it
# 6. Split each line into words
# 7. For each word in a line, check if it is a reserved word
# 7a. If it is a reserved word, add to the count
# 8. Display total number of reserved words
#

def populateReservedWordsDict():
    reservedWords = {"False": 0, "None": 0, "True": 0, "and": 0,
                    "as": 0, "assert": 0, "break": 0, "class": 0,
                    "continue": 0, "def": 0, "del": 0, "elif": 0,
                    "else": 0, "except": 0, "finally": 0, "for": 0,
                    "from": 0, "global": 0, "if": 0, "import": 0,
                    "in": 0, "is": 0, "lambda": 0, "nonlocal": 0,
                    "not": 0, "or": 0, "pass": 0, "raise": 0,
                    "return": 0, "try": 0, "while": 0, "with": 0,
                    "yield": 0}

    return reservedWords

def main():
    reservedWords = populateReservedWordsDict()

    print("Count the number of reserved words in a python file.")
    filename = input("Enter the name of a file: ")
    inFile = open(filename, "r")

    # for each line in the file
    #  strip the line of leading and trailing whitespace
    #  if the line is not empty, not a comment, nor a print statement
    #   split each line into words
    #   for each word check if it is a reserved word
    #    if it is, add to the count
    for line in inFile:
        line = line.strip()

        if line != "" and not (line[0] == "#" or line[:5] == "print"):
            for word in line.split():
                if word in reservedWords:
                    reservedWords[word] = reservedWords[word] + 1

    inFile.close()
    print("\nNumber of reserved words:", sum(reservedWords.values()))
    input()

main()
