def calculate_change(cents):
    quarters = int(cents/25)
    cents = cents - (quarters*25)
    dimes = int(cents/10)
    cents = cents - (dimes*10)
    nickels = int(cents/5)
    cents = cents - (nickels*5)
    pennies = cents
    coins = quarters + dimes + nickels + pennies

    return coins, quarters, dimes, nickels, pennies


def print_change(cents, coins, quarters, dimes, nickels, pennies):
    if quarters == 1:
        print(f"{coins} coins {quarters} Quarter", end=" ")
    elif quarters > 1:
        print(f"{coins} coins {quarters} Quarters", end=" ")
    else:
        print(f"{coins} coins ", end=" ")

    if dimes == 1:
        print(f"{dimes} Dime", end=" ")
    elif dimes > 1:
        print(f"{dimes} Dimes", end=" ")

    if nickels == 1:
        print(f"{nickels} Nickel", end=" ")
    elif nickels > 1:
        print(f"{nickels} Nickels", end=" ")

    if pennies == 1:
        print(f"{pennies} Penny", end=" ")
    elif pennies > 1:
        print(f"{pennies} Pennies", end=" ")
    print()


answer = 'Y'
while answer.lower() == 'y':
    file = input("Please enter the name of the file to be processed: ")
    
    try:
        with open(file) as input_data:
            print("List of changes to prepare")
            for each_line in input_data:
                cents = int(each_line.strip())
                coins, quarters, dimes, nickels, pennies = calculate_change(cents)
                print(cents, "cents:", end=" ")
                print_change(cents, coins, quarters, dimes, nickels, pennies)

    except:
        print('Error accessing file ')
    answer = input("Do you want to enter another file[y/n]? ")
