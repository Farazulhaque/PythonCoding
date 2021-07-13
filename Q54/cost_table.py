items = ["Beans", "Rice", "Banana", "Ice", "Tea", "Bread", "Orange", "Sugar"]
prices = [3.25, 4.31, 6.88, 3.3, 5.25, 4.89, 6.32, 2.25]


def main():
    make_cost_table()


def make_cost_table():
    max_qty = int(input("Enter Quantity(1-9): "))
    horizontal = input("Horizontal or Vertical?(h/v): ")
    build_cost_table(items, prices, max_qty, horizontal)


def build_cost_table(items, prices, max_qty, horizontal):
    if horizontal.lower() == "h":
        print("Cost Table")
        print("%8s" % ("Item/Qty"), end="")
        for i in range(1, max_qty+1):
            print("%8d" % i, end="")
        print()
        for i in range(len(items)):
            print("%-8s" % items[i], end="")
            for j in range(1, max_qty+1):
                x = prices[i] * j
                print("%8.2f" % x, end="")
            print()
    elif horizontal.lower() == "v":
        print("Cost Table")
        print("%8s" % ("Qty/Item"), end="")
        for i in range(len(items)):
            print("%8s" % items[i], end="")
        print()
        for i in range(1, max_qty+1):
            print("%-8d" % i, end="")
            for j in range(len(prices)):
                x = i * prices[j]
                print("%8.2f" % x, end="")
            print()


main()
