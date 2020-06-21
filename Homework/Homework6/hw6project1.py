#! /usr/bin/python
# File Name:     hw6project1.py
# Programmer:    Raul Aguilar
# Date:          June 20, 2020
#
# CS 138 1535 Homework 6 Project 1
# Define functions for sphereArea(radius) to return the surface area of a
# sphere given its radius and sphereVolume(radius) to return the volume of a
# sphere given its radius.
#
# Algorithm:
# 1. Calculate surface area and volume of two spheres
# 2. Print results
import math

def sphereArea(r):
    '''Returns the surface area of a sphere with radius r.'''
    return 4*math.pi*(r**2)

def sphereVolume(r):
    '''Returns the volume of a sphere with radius r.'''
    return 4*math.pi*((r**3)/3)

def printSphere(radius):
    ''' Prints the surface area and volume of a sphere with the passed
    radius. '''

    print("Radius:", radius)
    print("Surface area:", sphereArea(radius))
    print("Volume:", sphereVolume(radius))

def main():
    radius1, radius2 = 16, 65
    printSphere(radius1)
    print()
    printSphere(radius2)

main()