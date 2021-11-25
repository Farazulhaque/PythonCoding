def main():
    l1 = readData()
    print("Original list: ", end="")

    for i in range(len(l1)):
        print(l1[i], end="")
        if i != len(l1) - 1:
            print(", ", end="")

    l1 = evenToFront(l1)

    print("\nList after moving evens to the front: ", end="")
    for i in range(len(l1)):
        print(l1[i], end="")
        if i != len(l1) - 1:
            print(", ", end="")


def readData():
    l1 = []
    for i in range(8):
        l1.append(int(input()))
    return l1


def evenToFront(l1):
    newList = []
    j = 0
    for i in range(len(l1)):
        if (l1[i] % 2 == 0):
            newList.insert(j, l1[i])
            j += 1
        else:
            newList.append(l1[i])
    return newList


main()
