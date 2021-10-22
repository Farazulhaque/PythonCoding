d1 = {'Aspirin': 15, 'Tylenol': 20, 'Lipitor': 18, 'Prilosec': 24, 'Glucophage': 19, 'Zocor': 29, 'Toprol': 32,
      'Zithromax': 42, 'Zoloft': 25, 'Xanax': 42, 'Wellbutrin': 52, 'Flexeril': 19, 'Prozac': 100, 'Effexor': 40, 'Adderall': 20}

d2 = {1: 'Aspirin', 2: 'Tylenol', 3: 'Lipitor', 4: 'Prilosec', 5: 'Glucophage', 6: 'Zocor', 7: 'Toprol', 8: 'Zithromax', 
        9: 'Zoloft', 10: 'Xanax', 11: 'Wellbutrin', 12:'Flexeril', 13: 'Prozac', 14: 'Effexor', 15: 'Adderall'}


def MainMenu():
    while True:
        print()
        print("**** Main Menu ****")
        print("Press 1: medication status")
        print("\t2: add medication to inventory")
        print("\t3: remove medication from inventory")
        print("\t4: quit  --> ", end="")
        choice = int(input())
        if choice == 1:
            print_status()
        elif choice == 2:
            add_pills()
        elif choice == 3:
            remove_pills()
        elif choice == 4:
            print("Program ending. Have a superior day.")
            break
        else:
            print("Invalid choice.")


def print_status():
    print()
    print("-"*20)
    print("Medication Inventory:")
    print("-"*20)
    print("%-5s %-10s %5s" % ("##", "Name", "Qty"))

    for i in range(len(d1)):
        print("%-5s %-10s %5s" % (i+1, d2[i+1], d1[d2[i+1]]))


def add_pills():
    print_status()
    print("Which medication you want to deposit?")
    medication_number = int(input("Enter the medication number: "))
    print(f"How many pills of {d2[medication_number]} to add? --> ", end="")
    number_add = int(input())
    d1[d2[medication_number]] += number_add
    print(
        f"\tUPDATE: {d2[medication_number]} new balance: {d1[d2[medication_number]]}")


def remove_pills():
    print_status()
    print("Which medication you want to remove?")
    medication_number = int(input("Enter the medication number: "))
    print(f"How many pills of {d2[medication_number]} do you want to remove?")
    print(f"\tMaximum available is {d1[d2[medication_number]]}")
    print("Enter amount? --> ", end="")
    number_add = int(input())
    d1[d2[medication_number]] -= number_add
    print(
        f"\tUPDATE: {d2[medication_number]} new balance: {d1[d2[medication_number]]}")
MainMenu()

