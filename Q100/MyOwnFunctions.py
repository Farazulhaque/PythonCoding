# Name:
# Date
# Program Name:


def numbers():
    l1 = []

    for i in range(1, 14):
        l1.append(i)

    return l1


def sumAll(l1):
    sum = 0
    for i in range(len(l1)):
        sum += l1[i]

    return sum


def multiplyAll(l1):
    mul = 1
    for i in range(len(l1)):
        mul *= l1[i]

    return mul


def printEven(l1):
    for i in range(len(l1)):
        if l1[i] % 2 == 0:
            print(l1[i], end=",")


l1 = numbers()
print(f"Sum total : {sumAll(l1)}")
print(f"Multiply total : {multiplyAll(l1)}")
printEven(l1)
