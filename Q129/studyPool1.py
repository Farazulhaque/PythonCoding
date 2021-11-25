# Welcome to the simple math helper.
# What would you like to calculate?
# 1. Sqrt
# 2. Log
# 3. Factorial
# > 1
# Enter the number to sqrt:
# > 9
# 3

import math


def main():
    # printing menu
    print("Welcome to the simple math helper.")
    print("What would you like to calculate?")
    print("1. Sqrt")
    print("2. Log")
    print("3. Factorial")
    # getting user choice
    choice = int(input("> "))

    # if user want to sqrt
    if choice == 1:
        print("Enter the number to sqrt:")
        # get number to sqrt
        num = int(input("> "))
        # print returned value from findSquareRoot(num)
        print(findSquareRoot(num))

    # if user want to log
    elif choice == 2:
        print("Enter the number to log:")
        # get number to log
        num = int(input("> "))
        # print returned value from findLog(num)
        print(findLog(num))

    # if user want to factorial
    elif choice == 3:
        print("Enter the number to factorial:")
        # get number to factorial
        num = int(input("> "))
        # print returned value from findFactorial(num)
        print(findFactorial(num))

    # if user enter anything else then print invalid choice
    else:
        print("Invalid Choice.")


# function to find square root
def findSquareRoot(num):
    return math.sqrt(num)


# function to find log
def findLog(num):
    return math.log(num)


# function to find factorial
def findFactorial(num):
    return math.factorial(num)


main()
