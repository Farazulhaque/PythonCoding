def printmenu():
    print("%-12s %-20s %-10s" % ("Dish No", "Dish name", "Price"))
    print("-"*8 + "    " + "-"*15 + "     " + "-"*8)
    print("%-12s %-20s %-10s" % ("1", "Gang Gai", "$10.00"))
    print("%-12s %-20s %-10s" % ("2", "Pad Thai", "$8.75"))
    print("%-12s %-20s %-10s" % ("3", "Pad Cashew", "$9.50"))
    print("%-12s %-20s %-10s" % ("4", "Pad Prik", "$10.25"))
    print("%-12s %-20s %-10s" % ("5", "Peanut Curry", "$9.50"))
    print("%-12s %-20s %-10s" % ("6", "Curry Noodle", "$11.25"))


def getitemCost():
    item_cost = 0
    choice = int(input("Enter the item number you want(1-6): "))
    while choice > 6 or choice < 1:
        print("Invalid item number choice")
        choice = int(input("Enter the item number you want(1-6): "))
    if choice == 1:
        item_cost += 10.00
    elif choice == 2:
        item_cost += 8.75
    elif choice == 3:
        item_cost += 9.50
    elif choice == 4:
        item_cost += 10.25
    elif choice == 5:
        item_cost += 9.50
    elif choice == 6:
        item_cost += 11.25
    return item_cost


def getAge():
    above65 = input("Are you 65 years old or older[Y/n]: ").lower()
    while above65 not in ['y', 'n']:
        print("Invalid choice.")
        above65 = input("Are you 65 years old or older[Y/n]: ").lower()

    return above65


def calculations(total_cost):
    item_cost = getitemCost()
    above65 = getAge()

    if above65 == 'y':
        item_cost *= 1.10

    total_cost += item_cost
    return total_cost


def main():
    global total_cost
    total_cost = 0
    printmenu()
    total_cost = calculations(total_cost)

    another_item = input("Would youlike to order another item[Y/n]: ").lower()
    while another_item not in ['y', 'n']:
        print("Invalid choice.")
        another_item = input(
            "Would youlike to order another item[Y/n]: ").lower()
    while another_item == 'y':
        printmenu()
        total_cost = calculations(total_cost)

    gift_card = input("Do you have a gift card[Y/n]: ").lower()
    while gift_card not in ['y', 'n']:
        print("Invalid choice.")
        gift_card = input("Do you have a gift card[Y/n]: ").lower()

    if gift_card == 'y':
        gift_discount = int(
            input("How much money would you like to apply from card? "))
        tax = total_cost * 0.06
        print("Bill Information")
        print("-"*40)
        print("%-30s $%s" % ("Total of all items", total_cost))
        print("%-30s $%s" % ("Taxes", tax))
        print(" " * 30, end="")
        print("-"*5)
        print("%-30s $%s" % ("Bill", total_cost+tax))

    else:
        tax = total_cost * 0.06
        print("Bill Information")
        print("-"*40)
        print("%-30s $%s" % ("Total of all items", total_cost))
        print("%-30s $%s" % ("Taxes", tax))
        print(" " * 30, end="")
        print("-"*5)
        print("%-30s $%s" % ("Bill", total_cost+tax))


main()
