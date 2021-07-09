# a-)List all Fibonacci numbers on console screen up to n terms. n is given as a screen input
def a():
    n = int(input("How many terms? "))

    # first two terms
    n1, n2 = 0, 1
    count = 0

    # check if the number of terms is valid
    if n <= 0:
        print("Please enter a positive integer")
    # if there is only one term, return n1
    elif n == 1:
        print("Fibonacci sequence upto", n, ":")
        print(n1)
    # generate fibonacci sequence
    else:
        print("Fibonacci sequence:")
        while count < n:
            print(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1


a()


# b-)User inputs two integers m and n. List all Fibonacci numbers on console screen between these two integers m,n
def b():
    first = 5
    next = first + 1
    last = 50
    print(f"Fibonacci sequence between {first} and {last}:")
    while True:
        if first <= last:
            print(first)
            nth = first + next
            # update values
            first = next
            next = nth
        else:
            break


b()
