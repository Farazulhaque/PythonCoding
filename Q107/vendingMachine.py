items = [["Candy bar", 3], ["Chips", 5],
         ["Soda", 4], ["Gummy worms", 2]]


def displayChoices():
    print()
    print("1. %-15s - %-15s" % ("Candy bar", "3 quarters"))
    print("2. %-15s - %-15s" % ("Chips", "5 quarters"))
    print("3. %-15s - %-15s" % ("Soda", "4 quarters"))
    print("4. %-15s - %-15s" % ("Gummy worms", "2 quarters"))


def makeSelection(noOfQuarters):
    itemToBuy = int(input("Enter number of item you wish to buy: "))
    if items[itemToBuy-1][1] <= noOfQuarters:
        print(f"Vending {items[itemToBuy-1][0]}.")
        noOfQuarters -= items[itemToBuy-1][1]
    else:
        print("You don't have enough money.")

    print(f"You have {noOfQuarters} quarters left to spend.")
    cont = input("Would you like to continue buying items? (Y or N): ")
    if cont.lower() == "y":
        displayChoices()
        makeSelection(noOfQuarters)
    else:
        exit(0)


def main():
    noOfQuarters = int(input("Enter number of quarters you have: "))
    displayChoices()
    makeSelection(noOfQuarters)


main()
