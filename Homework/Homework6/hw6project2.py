#! /usr/bin/python
# File Name:     hw6project1.py
# Programmer:    Raul Aguilar
# Date:          June 20, 2020
#
# CS 138 1535 Homework 6 Project 2
# Write a program to print the lyrics for ten verses of "The Ants Go Marching."
#

def antsGoMarching(number, activity):
    print("The ants go marching {} by {}, hurrah, hurrah".format(number, number))
    print("The ants go marching {} by {}, hurrah, hurrah".format(number, number))
    print("The ants go marching {} by {},".format(number, number))
    print("The little stops to", activity)
    print("And they all go marching down to the ground")
    print("To get out of the rain, BOOM! BOOM! BOOM!\n")

def main():
    antsGoMarching("one", "suck his thumb")
    antsGoMarching("two", "tie his shoe")
    antsGoMarching("three", "climb a tree")
    antsGoMarching("four", "shut the door")
    antsGoMarching("five", "take a dive")
    antsGoMarching("six", "pick up sticks")
    antsGoMarching("seven", "go to heaven")
    antsGoMarching("eight", "shut the gate")
    antsGoMarching("nine", "check the time")
    antsGoMarching("ten", "say \"The End\"")


main()
