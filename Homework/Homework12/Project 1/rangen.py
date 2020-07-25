import random

def main():
    outfile = open("100000num.txt", "w")

    for i in range(90000):
        print(random.randint(-10000000, 10000000), file=outfile)

    outfile.close()


main()
