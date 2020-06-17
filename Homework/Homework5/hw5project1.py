#
# author    Raul Aguilar
# date      June 16, 2020
# CS 138 1535 Homework 5 Project 1
# Write a program that allows the user to type in a phrase and then outputs the
# acronym for that phrase.
#

def main():
    chars = []
    phrase = input("Enter a phrase to turn into an acronym:\n")
    for word in phrase.split():
        chars.append(word[0])

    acronym = "".join(chars).upper()
    print("\nYour acronym is:", acronym)

main()