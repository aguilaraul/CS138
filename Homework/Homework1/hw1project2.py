#! /usr/bin/python
# Exercise No.  2
# File Name:    hw1project2.py
# Author:       Raul Aguilar
# Date:         June 14, 2020
#
# Problem Statement:
#  Write a program that computes the percentage for a test
#

def main():
    correct = eval(input("Please enter the number of questions answered correctly: "))
    total = eval(input("Please enter the total number of questions: "))

    score = (correct / total) * 100.0
    print("Score: ", score)


main()
