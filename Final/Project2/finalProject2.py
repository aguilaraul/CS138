#
# author    Raul Aguilar
# date      July 26, 2020
#
# CS 138 1535 Final Project 2
# Write a program that reads both the girl’s and boy’s files into
# memory using a dictionary.Allow the user to input a name, the program
# should find the name in the dictionary and print out the rank and the
# number of namings. If the name isn’t a key in the dictionary then the
# program should note this and say that no match exists.
# 
# Algorithm:
# 1. Populate girl/boy names by reading in the file with name and count
#   Line number is rank of name
#   For each line in the file, split it into name and count, add name
#   to dictionary with NameInfo object containing rank and count, and
#   increment rank
#   Close name file and return the names dictionary
# 2. Accept user input for name
# 3. Look for name in dictionary
#   If name in dict, print name, rank, and count
#   If name not in dict, print name is not ranked among 1000
#
class NameInfo:
    def __init__(self, rank, count):
        self.rank = rank
        self.count = count


def populateNames(filename):
    names = dict()
    namesList = open(filename, "r")
    rank = 1
    for line in namesList:
        name, count = line.split()
        names[name] = NameInfo(rank, count)
        rank += 1
    namesList.close()
    return names


def main():
    # Populate names dictonaires
    girlNames = populateNames("girlnames.txt")
    boyNames = populateNames("boynames.txt")

    # Retrieve user input and search for names
    name = input("Enter a name to look for: ")
    
    if name in girlNames:
        print("{} is ranked {} in popularity among girls with {} namings.".format(name, girlNames[name].rank, girlNames[name].count))
    else:
        print("{} is not ranked among the top 1000 girl names.".format(name))

    if name in boyNames:
        print("{} is ranked {} in popularity among boys with {} namings.".format(name, boyNames[name].rank, boyNames[name].count))
    else:
        print("{} is not ranked among the top 1000 boy names.".format(name))


main()