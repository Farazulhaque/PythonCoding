def get_valid_amount_atm_feedback():
    print()
    amount = int(input("Enter an amount multiple of 10 and greater than 30: "))
    while True:
        if amount % 10 != 0 and amount <= 30:
            print("Your amount is not a multiple of 10 and is less or equal to 30.")
        elif amount % 10 != 0:
            print("Your amount is not a multiple of 10.")
        elif amount <= 30:
            print("Your amount is less or equal to 30.")
        else:
            return amount
        amount = int(
            input("Enter a new amount multiple of 10 and greater than 30: "))


def main():
    amount = get_valid_amount_atm_feedback()
    print("Thanks, you withdrew $" + str(amount))
    print()


main()
