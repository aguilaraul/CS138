#
# author    Raul Aguilar
# date      June 15, 2020
#
# CS 138 1535 Homework 3 Extra Credit
# Write a program that prompts the user for a 4-digit year and then outputs the
# value of the Gregorian epact
#

def main():
    year = eval(input("Enter a 4-digit year: "))
    c = year//100
    epact = (8+(c//4) - c + ((8*c + 13)//25) + 11*(year%19))%30
    
    print("The epcat value is", epact, "days.")


main()