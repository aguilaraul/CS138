# nameinfo.py
# author    Raul Aguilar
# date      July 26, 2020
#
# CS 138 1535 Final Project 2
# Custom object containing rank and count of name among top 1000 names
#
class NameInfo:
    def __init__(self, rank, count):
        self.rank = rank
        self.count = count