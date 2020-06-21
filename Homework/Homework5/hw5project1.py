#! /usr/bin/python
# File Name:     hw5project1.py
# Programmer:    Raul Aguilar
# Date:          June 20, 2020
#
# CS 138 1535 Homework 5 Project 1
# Write a program that allows the user to type in a phrase and then outputs the
# acronym for that phrase.
#
# Algorithm:
# 1. Ask user for phrase to turn into acronym
# 2. Split the phrase at each space
# 3. Take the first letter of each split word
# 4. Make them uppercase
# 5. Print out the acronym

def main():
    chars = []
    phrase = input("Enter a phrase to turn into an acronym:\n")
    for word in phrase.split():
        chars.append(word[0])

    acronym = "".join(chars).upper()
    print("\nYour acronym is:", acronym)

main()