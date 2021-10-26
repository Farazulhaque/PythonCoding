def menu():
    print("a. Miles to kilometer")
    print("b. Gallons to liters")
    print("c. Pounds to kilogram")
    print("d. Inches to centimeter")
    print("e. Fahrenheit to celsius")


def main():
    menu()
    choice = input("Enter your choice: ").lower()
    while choice not in ['a', 'b', 'c', 'd', 'e']:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice: ").lower()
    with open("conversion.txt", "w") as file:
        file.write(f"%-20s %-20s %-20s %-20s\n" % ("Original Unit",
                   "Original Value", "Converted Unit", "Converted Value"))
        file.write("-"*80)
        file.write("\n")
        for i in range(10):
            originalValue = float(input("Enter value to convert: "))
            if choice == 'a':
                originalUnit = "Miles"
                convertedUnit = "Kilometer"
                convertedValue = originalValue * 1.609344
            file.write(f"%-20s %-20s %-20s %-20s\n" % (originalUnit, "{0:.2f}".format(
                originalValue), convertedUnit, "{0:.2f}".format(convertedValue)))


main()
