def main():
    # getting user input
    lower = int(input("Enter lower bound: "))
    upper = int(input("Enter upper bound: "))
    print(f"Prime numbers between {lower} and {upper}: ", end="")
    for i in range(lower, upper):
        if isPrime(i):
            print(i, end=" ")


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
