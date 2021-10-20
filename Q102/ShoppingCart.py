price = []


def main():
    cart = []

    # getting list of item name and price stored in file
    # and store it in python list items and price
    items = []
    fileName = open("items.txt", "r")
    for line in fileName:
        fields = line.split(",")
        items.append(fields[0])
        price.append(float(fields[1].lstrip().rstrip()))

    print("Welcome to shopping at Amazing209!")
    choice = ""
    while choice != "quit":

        print("\n1. Purchase Clothes")
        print("\n2. Checkout\n")

        choice = input(
            "Please input an option or type 'quit' to exit the program: ")
        if choice == "1":
            print("\nList of available items")
            print("-"*23)
            for i in range(len(items)):
                print(f"%-15s - %.2f" % (items[i], price[i]))

            print()
            name = input("Enter the item name to purchase: ").title()
            quantity = int(input("Enter the quantity: "))
            if add_to_cart(name, quantity, cart, items):
                print(f"\n{quantity} of {name} is added to your cart")
            else:
                print("Item not available")
        elif choice == "2":
            print("\nThanks for shopping with us")
            print("You purchased the following item(s):")
            total = checkout(cart)
            print(f"\nThe total amount is: $ {total}")


def add_to_cart(name, quantity, cart, items):
    found = False
    for i in range(len(items)):
        if items[i].lower() == name.lower():
            details = []
            details.append(name)
            details.append(price[i])
            details.append(quantity)
            cart.append(details)
            return True
    if found == False:
        return False


def checkout(cart):
    total = 0
    for i in range(len(cart)):
        print(f"%-15s - %.2f - %5d" % (cart[i][0], cart[i][1], cart[i][2]))
        total += float(cart[i][1]) * float(cart[i][2])

    return total


main()
