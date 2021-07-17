# import random module to generate random numners
from random import randint


def main():
    # Create empty list to store numbers
    num = []
    # Loop 8 times
    for i in range(8):
        # Add number into num list
        num.append(randint(0, 9))
    print("Eight-digit account number: ", end="")
    # Printing account number
    for i in range(len(num)):
        print(num[i], end="")


# Calling main()
main()
