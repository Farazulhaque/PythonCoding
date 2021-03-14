import sys


def getUserInput():
    global name
    global quantity
    global unitcost
    global inkcost
    global boolhelp

    print("--Custom Print Quote--")
    print()
    print("Enter the following information to create a quote:")
    name = input("Product name: ")
    # create a string of valid characters for product name
    alpha = "abcdefghijklmnopqrstuvwxyz "
    for letter in name.lower():
        if letter in alpha:
            continue
        else:
            print("Product name must contain only letters and spaces")
            # exit the program
            sys.exit(0)

    quantity = input("Quantity: ")
    # check if the quantity is digit and whole number
    if quantity.isdigit() and int(quantity) > -1:
        quantity = int(quantity)
    else:
        print("Quantity must be numeric and whole number")
        sys.exit(0)

    unitcost = str(input("Our unit cost for the "+name.upper()+": "))
    # create a string of valid characters for unitcost
    alpha = "$.1234567890"
    for letter in unitcost:
        if letter in alpha:
            continue
        else:
            print("Cost must be numeric")
            sys.exit(0)
    # remove $ for calculations
    unitcost = float(unitcost.replace("$", ""))

    inkcost = input("How many colors will be printed? ")
    if inkcost.isdigit() and int(inkcost) > -1:
        inkcost = int(inkcost)
    else:
        print("Ink colors must be numeric and whole number")
        sys.exit(0)
    help = input("Does customer require design help? ")
    help = help.lower()
    # boolean variable to store if help is required or not

    boolhelp = False
    if help == "yes" or help == "y":
        boolhelp = True
    elif help == "no" or help == "n":
        pass
    else:
        print("Please answer Yes or No")
        sys.exit(0)
    print("------------------------------------------")


def getDiscountCalculations():
    # calculate the various charges
    setupcharge = 7*inkcost
    designcharge = inkcost*unitcost*8
    materialcost = unitcost*quantity
    total = 0
    if boolhelp:
        # multiply with 1.2 for 20% charge
        total = (setupcharge+designcharge+materialcost)*1.2
    else:
        total = (setupcharge+materialcost)*1.2

    print("Product type:", name.upper())
    print()
    # round off the cost to 2 decimal points
    print("Material cost: $"+str(round(materialcost, 2)))
    print(inkcost, "color setup: $"+str(round(setupcharge, 2)))

    if boolhelp:
        print("Custom design: $"+str(round(designcharge, 2)))
    print("Total: $"+str(round(total, 2)))

    if "mug" in name.lower():
        # multiply with 0.9 for 10% discount
        total = total*0.9

    print("Discounted total for", name.upper()+": $"+str(round(total, 2)))


def main():
    getUserInput()
    getDiscountCalculations()


main()
