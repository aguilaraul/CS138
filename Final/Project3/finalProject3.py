#
#
#
from database import Database

def printMenu():
    print("What would you like to do?")
    print("1. Enter a new employee")
    print("2. Remove an exisiting employee")
    print("3. Calulate monthly pay of all employees")
    print("3. Save the current database to a file")
    print("4. Load an existing database from a file")

def main():
    db = Database()
    choice = 0
    while choice != -1:
        printMenu()
        choice = int(input("Enter an option: "))

        if choice == 1:
            db.addEmployee()
        if choice == 3:
            db.save()


main()