#! /usr/bin/python
# File Name:     hw3project2.py
# Programmer:    Raul Aguilar
# Date:          June 20, 2020
# 
# CS 138 1535 Homework 3 Project 2
# Write a program to determine the length of a ladder required to reach
# a given height when leaned against a house
#
# Algorithm:
# 1. Enter the height required to reach
# 2. Enter the angle of the ladder
# 3. Convert degrees into radians and find length of the ladder
# 4. Display the length of the ladder required
#
import math

def main():
    height = eval(input("Enter the height required to reach: "))
    angle = eval(input("Enter the angle of the ladder in degrees: "))
    
    length = height/math.sin((math.pi/180) * angle)

    print("The length of the ladder must be", length, "units long.")


main()