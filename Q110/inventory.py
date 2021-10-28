def main():
    inventory_name, inventory_counts, inventory_costs = read_inventory_file()
    print("Welcome to Trish's Inventory Input System")
    print("Current Inventory:")
    display_all_inventory(inventory_name, inventory_counts, inventory_costs)

    response = ''
    while response != '0':
        print("\n(1) Add, (2) Display, (3) Delete an item or (0) Exit")
        response = input('Enter your choice: ')
        print()
        if response == "1":
            item_name, item_count, unit_cost = get_item_input()
            inventory_name.append(item_name)
            inventory_counts.append(item_count)
            inventory_costs.append(unit_cost)
            print(f"{item_name} added to inventory.")

        elif response == "2":
            item_name = input('Enter item name: ')
            item_found = False
            for i in range(len(inventory_name)):
                if inventory_name[i] == item_name:
                    print(
                        f"{item_name}, Count:{inventory_counts[i]}, Cost:{inventory_costs[i]}")
                    item_found = True
                    break
            if item_found == False:
                print(f"{item_name}: Not Found")

        elif response == "3":
            item_name = input('Enter item name: ')
            item_found = False
            for i in range(len(inventory_name)):
                if inventory_name[i] == item_name:
                    inventory_name.remove(item_name)
                    inventory_counts.remove(inventory_counts[i])
                    inventory_costs.remove(inventory_costs[i])
                    print(f"{item_name} Deleted")
                    item_found = True
                    break
            if item_found == False:
                print(f"{item_name}: Not Found")
        elif response != "0":
            print("Invalid choice. Try again.\n")

    display_all_inventory(inventory_name, inventory_counts, inventory_costs)

    # save_inventory_file(inventory_counts, inventory_costs)


def display_all_inventory(inventory_name, inventory_counts, inventory_costs):
    print("%-20s %-8s  %-10s" % ("Item Name", "Count", "Unit Cost"))
    print("%-9s %-10s %-5s %-3s %-9s" % ("-"*9, " ", "-"*5, " ", "-"*9))
    for item in range(len(inventory_name)):
        print("%-20s %-8s  %-10s" %
              (inventory_name[item], inventory_counts[item], inventory_costs[item]))


def save_inventory_file(inventory_counts, inventory_costs):
    pass


def read_inventory_file():
    itemName = []
    itemCount = []
    unitCost = []
    with open("Q110\inventory.txt", "r") as file:
        for line in file:
            lst = line.split(",")
            itemName.append(lst[0])
            itemCount.append(lst[1])
            unitCost.append(float(lst[2]))
            # print(lst)
    # print(itemName, itemCount, unitCost)

    return itemName, itemCount, unitCost

# read_inventory_file()


def get_item_input():
    item_name = input("Enter the item name: ")
    item_count = int(input("Enter the item count: "))
    unit_cost = float(input("Enter the unit cost: "))

    return item_name, item_count, unit_cost


main()
