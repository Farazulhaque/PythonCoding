def calc_cost():
    ppu = int(input("Enter a price-per-unit (omit the $ sign): "))
    qty = int(input("How many did you want? "))
    return ppu * qty


while True:
    choice = input("Would you like to estimate a cost? (Yes/No: ")
    if choice.lower()[0] != 'y':
        break
    else:
        cost = calc_cost()
        print("Total cost: $", cost)
