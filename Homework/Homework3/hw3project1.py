#
# author    Raul Aguilar
# date      June 15, 2020
#
# CS 138 1535 Homework 3 Project 1
# Write a program that calculates the cost per square inch of a circular pizza,
# given its diameter and price
#

import math

def main():
    price = eval(input("Enter the price of the pizza: "))
    diameter = eval(input("Enter diameter of the pizza: "))
    radius = diameter/2
    area = math.pi*(radius**2)
    cost = price / area
    print("The cost per square is", cost)


main()