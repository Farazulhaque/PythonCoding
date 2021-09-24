# create empty list to store items data
DescriptionList = []
PriceList = []
quantityList = []
totalList = []

# loop 6 times to store data in list
for i in range(6):
    # get inputs
    description = input("Enter the description of your item: ")
    price = float(input("Enter the price of your item: "))
    quantity = int(input(f"Enter the quantity of {description}: "))
    total = price * quantity
    # Append to list
    DescriptionList.append(description)
    PriceList.append(price)
    quantityList.append(quantity)
    totalList.append(total)
    # new line
    print()

# new line
print()
print("Here is your shopping cart")
# for decorations
print("."*55)
print("%-10s %9s %13s %15s" %
      ("Description", "Price", "Quantity", "Total Value"))
print("."*55)
# printing all
for i in range(6):
    print("%-10s %10s $ %10s %15s $" % (DescriptionList[i], "{:.2f}".format(
        PriceList[i]), quantityList[i], "{:.2f}".format(totalList[i])))
print("."*55)
print("Total Sales is %35s $" % "{:.2f}".format(sum(totalList)))
print(
    f"Highest priced item is {DescriptionList[PriceList.index(max(PriceList))]}")
print("."*55)
