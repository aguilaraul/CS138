#
# author    Raul Aguilar
# date      July 9, 2020
#
# CS 138 1535 Homework 12 Extra Credit
# Base-10 to any other base converter, but not back to base 10.
# Write a program that allows a user to enter a number and a base and
# then prints out the digits of the number in the new base.
#
# Alogrithm:
# 1. Take number and base from user
# 2. Append remainder of num%base into list
# 3. Recursively run conversion method using num//base until quotient is
#    zero
# 4. Reverse the list, return the list
# 


def baseConversion(num, base):
    result = []
    result = conversion(num, base, result)
    result.reverse()
    return result


def conversion(num, base, result):
    if num == 0:
        return result

    result.append(num%base)
    return conversion(num//base, base, result)


def main():
    validNum = False
    validBase = False

    while not validNum:
        try:
            num = int(input("Enter number to convert: "))
            validNum = True
        except:
            print("Number is not valid. Re-enter.\n")

    while not validBase:
        try:
            base = int(input("Enter base to convert to: "))
            validBase = True
        except:
            print("Base is not valid. Re-enter.\n")

    print(baseConversion(num, base))


main()
