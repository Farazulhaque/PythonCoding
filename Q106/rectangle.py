def main():
    while True:
        l = getLength()
        w = getWidth()
        area = getArea(l, w)
        displayData(l, w, area)
        print()
        choice = input("Do you want to enter more calculation?[Y/n]: ").lower()
        if choice == 'n':
            break
        elif choice not in ['y', 'n']:
            print("Invalid chooice.")


def getLength():
    l = float(input("Enter length of the rectangle: "))
    while (isValid(l) == False):
        print("Invalid input. Enter positive number.")
        l = float(input("Enter length of the rectangle: "))
    return l


def getWidth():
    w = float(input("Enter width of the rectangle: "))
    while (isValid(w) == False):
        print("Invalid input. Enter positive number.")
        w = float(input("Enter width of the rectangle: "))
    return w


def getArea(l, w):
    area = l * w
    return area


def displayData(l, w, area):
    print(f"Area of rectangle having length: {l} and width: {w} is {area}")


def isValid(i):
    if i > 0:
        return True
    else:
        return False


main()
