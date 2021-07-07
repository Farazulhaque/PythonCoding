import math
print("*"*50)
print("Select one of the following geometrical shapes:")
print("C: Circle")
print("R: Rectangle")
print("P: Parallelogram")
print("*"*50)
loop = "y"
while loop.lower() == "y":
    choice = input("\nEnter your choice (C, R or P): ")
    if choice.lower() == "c":
        pi = 3.14
        r = int(input("Enter radius of the circle: "))
        perimeter = 2 * pi * r
        area = pi * r * r
        print("Shape\t\t\tPerimeter\t\t\tArea")
        print("*"*50)
        print("Circle\t\t\t{:.1f}\t\t\t\t{:.3f}".format(perimeter, area))
    elif choice.lower() == "r":
        w = int(input("Enter width: "))
        h = int(input("Enter height: "))
        perimeter = 2 * (w + h)
        area = w * h
        print("Shape\t\t\tPerimeter\t\t\tArea")
        print("*"*50)
        print("Rectangle\t\t{:.1f}\t\t\t\t{:.3f}".format(perimeter, area))
    elif choice.lower() == "p":
        s1 = int(input("Enter side1: "))
        s2 = int(input("Enter side2: "))
        a = int(input("Enter angle: "))
        while (a < 0 or a > 180):
            a = int(input("Enter angle: "))
        perimeter = 2 * (s1 + s2)
        if (a > 0 and a < 90):
            area = (s1 * s2) * math.sin(a)
        else:
            area = (s1 * s2) * math.sin(90-a)
        print("Shape\t\t\tPerimeter\t\t\tArea")
        print("*"*50)
        print("Parallelogram\t{:.1f}\t\t\t\t{:.3f}".format(perimeter, area))
    else:
        print("ERROR> Invalid choice: '{}'".format(choice))
    loop = input("Enter another shape?(Y/N): ")
