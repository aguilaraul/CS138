#
# author    Raul Aguilar
# date      July 9, 2020
#
# CS 138 1535 Homework 12 Extra Credit
# Write a program that allows a user to enter a number and a base and
# then prints out the digits of the number in the new base.
#
# Alogrithm:
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
    # @Debug
    # Take user input for num and base
    # but validate answers first for int
    print(baseConversion(1234, 20))

main()
