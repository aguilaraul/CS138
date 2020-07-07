#
# author    Raul Aguilar
# date      July 3, 2020
#
# CS 138 1535 Midterm Project 1
# Write a program that finds the mean, median, and standard deviation
# of a list of numbers which you read from a file.
#
# Algorithm:
#
import math
import statistics


def mean(list):
    if len(list) < 1:
        return None
    return sum(list) / len(list)


def median(list):
    """Assuming sorted list"""
    if len(list) < 1:
        return None
    middle = int(len(list) / 2)
    if len(list) % 2 != 0:
        return list[middle]
    else:
        return (list[middle] + list[middle - 1]) / 2


def stdDev(list):
    if len(list) < 2:
        return None
    else:
        S = 0
        M = mean(list)
        for X in list:
            S += (X-M)**2

        return math.sqrt(S / len(list)-1)

def stdDevRange(list):
    if len(list) < 2:
        return None
    else:
        sD = stdDev(list)
        M = mean(list)
        return [M-(2*sD), M+(2*sD)]


def run(filename):
    numbers = []
    inFile = open(filename, "r")

    for line in inFile:
        numbers.append(int(line))
    inFile.close()

    numbers.sort()
    print("{:<17} {}".format("Mean:", mean(numbers)))
    print("{:<17} {}".format("Median:", median(numbers)))
    print("{:<17} {}".format("Standard Dev:", stdDev(numbers)))
    print("{:<17} {}".format("Deviation Range:", stdDevRange(numbers)))
    print()


def main():
    files = ["0num.txt", "1num.txt", "2num.txt", "3num.txt", "15num.txt",
             "500num.txt", "859num.txt", "1000num.txt"]

    for file in files:
        print(file)
        run(file)

main()
