#
# author    Raul Aguilar
# date      July 6, 2020
#
# CS 138 1535 Homework 12 Project 2
#
#
# Algorithm:
#

def isPalendrome(str):
    i = str[0].lower()
    j = str[len(str)-1].lower()

    print(i)
    print(j)

    if i == j:
        if len(str) == 3:
            return True
        else:
            return isPalendrome(str[1:len(str)-1])
    else:
        return False


def main():
    print("Check if a phrase is a palendrome.")
    str = input("Enter a phrase: ")

    print(isPalendrome(str))

    if isPalendrome(str):
        print(str, "is a palendrome!!")
    else:
        print(str, "is not a palendrome.")


main()
