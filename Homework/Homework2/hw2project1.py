#! /usr/bin/python
# author    Raul Aguilar
# date      June 15, 2020
# CS 138 1535 Homework 2 Project 1
# Write a program that converts degrees Fahrenheit to Celsius

def main():
    fahrenheit = eval(input("Enter a temperature in Fahrenheit: "))
    celsius = 5*(fahrenheit-32)/9
    print("{} degrees Fahrenheit is".format(fahrenheit), end="")
    print(" {:.1f} degrees Celsius.".format(celsius))


main()