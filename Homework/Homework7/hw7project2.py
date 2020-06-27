#! /usr/bin/python
# File Name:     hw7project2.py
# Programmer:    Raul Aguilar
# Date:          June 20, 2020
#
# CS 138 1535 Homework 7 Project 2
# Poducksville speeding crisis is barreling out of control fast. Skid
# those speedsters to a stop by writing a program that accepts a speed
# limit and a clocked speed and either prints a message indicating the
# speed was legal or prints the amount of the fine, if the speed is
# illegal.
#
# Algorithm:
# 1. Ask for clocked speed
# 2. Ask for speed limit
# 3. If clocked speed > speed limit
#   3a. Add $50 fee for speeding
#   3b. Calculate mph over speed limit, multiple it by 5, and add to
# fee
#   3c. If clocked speed is over 90 mph, add $200 fee
#   3d. Print out penalty
# 4. Else print that the speed was legal
#

def speedingTicket(speedLimit, clockedSpeed):
    fee = 0
    if(clockedSpeed > speedLimit):
        fee = 50
        mphOver = clockedSpeed-speedLimit
        fee += 5*(mphOver)
        if(clockedSpeed > 90):
            fee += 200
        print("\n{} MPH over the {} MPH speed limit.".format(mphOver, speedLimit))
        print("${} penalty accrued.".format(fee))
    else:
        print()
        print(clockedSpeed, "MPH is within", speedLimit, "MPH.")
    

def main():
    clockedSpeed = int(input("Enter the clocked speed: "))
    speedLimit = int(input("Enter the speed limit: "))
    speedingTicket(speedLimit, clockedSpeed)

main()