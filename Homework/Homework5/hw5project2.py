#! /usr/bin/python
# File Name:     hw5project2.py
# Programmer:    Raul Aguilar
# Date:          June 20, 2020
#
# CS 138 1535 Homework 5 Project 2
#
# Algorithm:
# 1. Open the input file
# 2. Store each line containing two numbers
# 3. Close the input file, open the output file for writing
# 4. Split the numbers on each line
# 5. Add them together
# 6. Output the sum to file
# 7. Close file and exit
#

def main():
    # open the input file
    numbers = []
    inFile = open("input.txt", "r")
    
    # store each line containing two numbers
    for line in inFile:
        numbers.append(line)

    inFile.close()
    outFile = open("output.txt", "w")

    # split the numbers on each line, add them, and print to file
    for line in numbers:
        num1, num2 = line.split()
        num1 = eval(num1)
        num2 = eval(num2)
        print(num1 + num2, file=outFile)
    
    outFile.close
    print("Calculations complete.")

main()