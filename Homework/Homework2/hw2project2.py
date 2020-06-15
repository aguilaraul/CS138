#
# author    Raul Aguilar
# date      June 15, 2020
#
# CS 138 1535 Homework 2 Project 2
# Modify the avg2.py program (Section 2.5.3) to find the average of N (where N
# is any number) exam scores.
#

def main():
    average = 0
    numOfTest = eval(input("Enter the number of test: "))

    for i in range(numOfTest):
        average += eval(input("Enter the score for Exam {} ".format(i+1)))

    average /= numOfTest
    print("The average score is ", average)


main()