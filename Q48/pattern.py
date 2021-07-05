def upward(arrow):
    # It is used to print the space
    k = 9
    # Outer loop to print number of rows
    for i in range(1, 7):
        # Inner loop is used to print number of space
        for j in range(0, k):
            print(end=" ")
        # Decrement in k after each iteration
        k = k - 1
        # This inner loop is used to print stars
        for j in range(0, (i*2)-1):
            print(arrow, end="")
        print()


def downward(arrow):
    # It is used to print the space
    k = 4
    # Outer loop to print number of rows
    for i in range(6, -1, -1):
        # inner loop will print the spaces
        for j in range(k, 0, -1):
            print(end=" ")
        # Increment in k after each iteration
        k = k + 1
        # This inner loop will print number of stars
        for j in range(0, (i*2)-1):
            print(arrow, end="")
        if i != 1:
            print()


def row(height):
    for i in range(height):
        for j in range(0, 4):
            print(end=" ")
        print("|---------|")


def main():
    shape = input("Enter shape to display: ")
    arrow = input("Enter arrow character: ")
    height = int(input("Enter row-area height: "))
    if shape == "house":
        upward(arrow)
        row(height)
    elif shape == "plumbbob":
        upward(arrow)
        row(height)
        downward(arrow)
    elif shape == "hourglass":
        row(height)
        downward(arrow)
        upward(arrow)
        row(height)


main()
