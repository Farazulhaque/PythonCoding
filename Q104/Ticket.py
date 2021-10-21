ADULTPRICE = 55
CHILDRENPRICE = 25
DISCOUNTFOR4 = 10
DISCOUNTFOR5ORMORE = 15
print("Welcome to the Montclair Theme Park Ticketing System")

group_size = int(input("Please enter the size of your group: "))


if group_size == 2:
    numberOfAdults = int(input("Enter the number of adults: "))
    numberOfChildren = int(input("Enter number of children: "))
    party_size = numberOfAdults + numberOfChildren
    if party_size > group_size:
        print("You cannot have more people than the size you specified.")
    else:
        adult_total = numberOfAdults * ADULTPRICE
        children_total = numberOfChildren * CHILDRENPRICE
        total_cost = adult_total + children_total
        print("The total cost of the ", str(numberOfAdults), "adults and ",
              str(numberOfChildren), "children = $", str(total_cost))
elif group_size == 3:
    numberOfAdults = int(input("Enter the number of adults: "))
    numberOfChildren = int(input("Enter number of children: "))
    party_size = numberOfAdults + numberOfChildren
    if party_size > group_size:
        print("You cannot have more people than the size you specified.")
    else:
        adult_total = numberOfAdults * ADULTPRICE
        children_total = numberOfChildren * CHILDRENPRICE
        total_cost = adult_total + children_total
        print("The total cost of the ", str(numberOfAdults), "adults and",
              str(numberOfChildren), "children = $", str(total_cost))

elif group_size == 4:
    numberOfAdults = int(input("Enter the number of adults: "))
    numberOfChildren = int(input("Enter number of children: "))
    party_size = numberOfAdults + numberOfChildren
    if party_size > group_size:
        print("You cannot have more people than the size you specified.")
    else:
        adult_total = numberOfAdults * ADULTPRICE
        children_total = numberOfChildren * CHILDRENPRICE
        total_cost = adult_total + children_total
        discount = total_cost * DISCOUNTFOR4/100
        final_cost = total_cost - discount
        print("Total cost is ", str(total_cost))
        print("You received a discount of ", str(discount))
        print("The final cost of the ", str(numberOfAdults), "adults and",
              str(numberOfChildren), "children = $", str(final_cost))

elif group_size >= 5:
    group_size = int(input("Please enter the size of your group: "))
    numberOfAdults = int(input("Enter the number of adults: "))
    numberOfChildren = int(input("Enter number of children: "))
    party_size = numberOfAdults + numberOfChildren
    if party_size > group_size:
        print("You cannot have more people than the size you specified.")
    else:
        adult_total = numberOfAdults * ADULTPRICE
        children_total = numberOfChildren * CHILDRENPRICE
        total_cost = adult_total + children_total
        discount = total_cost * DISCOUNTFOR5ORMORE/100
        final_cost = total_cost - discount
        print("Total cost is ", str(total_cost))
        print("You received a discount of ", str(discount))
        print("The final cost of the ", str(numberOfAdults), "adults and",
              str(numberOfChildren), "children = $", str(final_cost))
else:
    if group_size == 0:
        print("Theank you for using the Montclair Theme Park Ticketing System")
    else:
        print("Invalid input")

