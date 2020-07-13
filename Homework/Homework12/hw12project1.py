#
# author    Raul Aguilar
# date      July 9, 2020
#
# CS 138 1538 Homework 12 Project 1
# Compare the results between linear search and binary search
#
# Algorithm:
#


def linearSearch(x, nums):
    loops = 0
    for i in range(len(nums)):
        loops += 1
        if nums[i] == x:
            return i, loops
    return -1, loops


def binarySearch(x, nums):
    loops = 0
    low = 0
    high = len(nums)-1

    while low <= high:
        loops += 1
        mid = (low+high)//2
        item = nums[mid]
        if x == item:
            return mid, loops
        elif x < item:
            high = mid-1
        else:
            low = mid+1

    return -1, loops


def main():
    key = 6056765
    files = ["numbers.txt", "10000num.txt", "100000num.txt"]

    for file in files:
        numbers = []
        infile = open(file, "r")

        for line in infile:
            numbers.append(int(line))

        print("Searching for {} in a list of {} numbers.".format(key, len(numbers)))
        print("Linear search results:")
        print(linearSearch(key, numbers))
        print("Binary search results:")
        numbers.sort()
        print(binarySearch(key, numbers))
        print()


main()
