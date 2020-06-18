#
# author    Raul Aguilar
# date      June 17, 2020
# CS 138 1535 Homework 7 Project 1
# Write a program that takes as input the gender of the child, the
# height of the mother in inches and the height of the father in
# inches. Output the estimated adult height of the child in inches.
#

def main():
    gender = input("Is the child male or female? ")
    motherHeight = eval(input("Enter the mother's height in inches: "))
    fatherHeight = eval(input("Enter the father's height in inches: "))
    if(gender == "male"):
        childHeight = ((motherHeight*13/12)+fatherHeight)/2
    else:
        childHeight = ((fatherHeight*12/13)+motherHeight)/2

    feet = int(childHeight//12)
    inches = int(childHeight%12)
    print("\nThe estimated height as an adult is {:.2f} inches".format(childHeight), end="")
    print(" or {} feet and {} inches.".format(feet, inches))


main()