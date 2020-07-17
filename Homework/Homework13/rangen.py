import random

def main():
    outfile = open("numbers.txt", "w")

    for i in range(5000):
        print(random.randint(-10000000, 10000000), file=outfile)

    outfile.close()


main()
