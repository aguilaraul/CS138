#! /usr/bin/python
# File Name:     hw3project1.py
# Programmer:    Raul Aguilar
# Date:          June 20, 2020
# 
# CS 138 1535 Homework 3 Project 1
# Write a program that calculates the cost per square inch of a circular pizza,
# given its diameter and price
#
# Algorithm:
# 1. Enter price of pizza
# 2. Enter diameter of pizza
# 3. Calculate area of pizza
# 4. Calculate price per square inch of pizza
# 5. Display results
#

import math

def main():
    price = eval(input("Enter the price of the pizza: "))
    diameter = eval(input("Enter diameter of the pizza: "))
    area = math.pi*((diameter/2)**2)
    print("The cost per square is", (price/area))


main()