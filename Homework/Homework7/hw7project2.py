#
# author    Raul Aguilar
# date      June 17, 2020
# CS 138 1535 Homework 7 Project 1
#

def speedingPenalty(speedLimit, clockedSpeed):
    fee = 0
    if(clockedSpeed > speedLimit):
        mphOver = clockedSpeed-speedLimit
        fee = 50
        fee += 5*(mphOver)
        if(clockedSpeed > 90):
            fee += 200
        print("\n{} MPH over the {} MPH speed limit.".format(mphOver, speedLimit))
        #print(mphOver, " mph over the", speedLimit, "mph speed limit. $", end="")
        print("${} penalty accrued.".format(fee))
    else:
        print()
        print(clockedSpeed, "MPH is within", speedLimit, "MPH.")
    

def main():
    speedLimit = eval(input("Enter the speed limit: "))
    clockedSpeed = eval(input("Enter the clocked speed: "))
    speedingPenalty(speedLimit, clockedSpeed)

main()