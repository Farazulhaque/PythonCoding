# Write a Python (or R) program that asks the user to enter an integer (X), then:

# Determines if X is prime or not
# If X is not prime, compute and print the factors of that integer X
# Evaluate and print the equation Y=8X²+ 1, for X values from -5 to 5 using the range function and for loop
def main():
    # getting user input
    x = int(input("Enter a number: "))

    # check a number is prime number or not
    # by using isPrime()
    # if it returns true then print number
    if (isPrime(x)):
        print(f"{x} is prime number.")
    # else print factors of the number entered by the user
    else:
        print(f"Factors of {x} is: ", end="")
        # loop from 1 to x
        for i in range(1, x+1):
            # and check each number is perfectly divisible by x or not
            if x % i == 0:
                # if any number is perfectly divisible by x then print that number
                print(f"{i} ", end="")


# function to check prime or not
def isPrime(x):
    # check only if it is greater than 1
    if x > 1:
        # loop from 2 to x
        for i in range(2, x):
            # and check each number
            # if any number is perfectly divisible by x
            # then it means it is not prime number
            # and return false
            if (x % i) == 0:
                return False
        # else return true
        return True
    # return false for all the number less than 1
    else:
        return False


# calling main function
main()
