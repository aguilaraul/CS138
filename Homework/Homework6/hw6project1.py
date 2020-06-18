#
# author    Raul Aguilar
# date      June 17, 2020
# CS 138 1535 Homework 6 Project 1
# Define functions for sphereArea(radius) to return the surface area of a
# sphere given its radius and sphereVolume(radius) to return the volume of a
# sphere given its radius.
#
import math

def sphereArea(radius):
    return 4*math.pi*(radius**2)

def sphereVolume(radius):
    return 4*math.pi*((radius**3)/3)

def printSphere(radius):
    print("Radius:", radius)
    print("Surface area:", sphereArea(radius))
    print("Volume:", sphereVolume(radius))

def main():
    radius1, radius2 = 16, 65
    printSphere(radius1)
    print()
    printSphere(radius2)

main()