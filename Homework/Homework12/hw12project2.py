#
# author    Raul Aguilar
# date      July 6, 2020
#
# CS 138 1535 Homework 12 Project 2
#
#
# Algorithm:
# 1. Base case: check if the string is 1 charater long
#   If so, middle of string and is a palindrome
# 2. Check if first and last index in string is a letter
#   If not, check if palindrome without that letter
# 3. If first and last letter match, check every letter in between
# 4. If first and last letter do not match, string is not a palindrome
#


def isPalindrome(str):

    if len(str) == 1:
        return True

    if str[0].isalpha():
        i = str[0].lower()
    else:
        return isPalindrome(str[1:])

    if str[-1].isalpha():
        j = str[-1].lower()
    else:
        return isPalindrome(str[:-1])

    if i == j:
        return isPalindrome(str[1:-1])
    else:
        return False


def main():
    print("Check if a phrase is a palindrome.")
    str = input("Enter a phrase: ")

    if isPalindrome(str):
        print(str, "is a palindrome!!")
    else:
        print(str, "is not a palindrome.")


main()
