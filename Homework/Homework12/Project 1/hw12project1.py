#
# author    Raul Aguilar
# date      July 13, 2020
#
# CS 138 1538 Homework 12 Project 1
# Compare the results between linear search and binary search
#
# Algorithm:
# 1. Open text files containing numbers
# 2. Read numbers into a list
# 3. Apply linear search algorithm and binary search algorithm on each
#   list
# 4. Display results
#
# Search algorithms from
# Python programming : an introduction to computer science\
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
    key = 2389240
    files = ["1000num.txt", "10000num.txt", "100000num.txt"]

    for file in files:
        numbers = []
        infile = open(file, "r")

        for line in infile:
            numbers.append(int(line))

        print("Searching for {} in a list of {} numbers.".format(key, len(numbers)))
        print("Linear search results:")
        index, loops = linearSearch(key, numbers)
        print("Index: {}, Iterations: {}".format(index, loops))
        print("Binary search results:")
        numbers.sort()
        index, loops = binarySearch(key, numbers)
        print("Index: {}, Iterations: {}".format(index, loops))
        print()


main()
