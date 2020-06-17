#
# author    Raul Aguilar
# date      June 16, 2020
# CS 138 1535 Homework 5 Project 2
#
#

def main():
    numbers = []
    inFile = open("input.txt", "r")
    
    for line in inFile:
        numbers.append(line)

    inFile.close()
    outFile = open("output.txt", "w")

    for line in numbers:
        num1, num2 = line.split()
        num1 = eval(num1)
        num2 = eval(num2)
        print(num1 + num2, file=outFile)
    
    outFile.close
    print("Calculations complete.")

main()