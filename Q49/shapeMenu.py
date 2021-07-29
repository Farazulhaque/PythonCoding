import math

loop = "y"
while loop.lower() == "y":
    print()
    print("*"*50)
    print("Select one of the following geometrical shapes:")
    print("C: Circle")
    print("R: Rectangle")
    print("P: Parallelogram")
    print("*"*50)
    choice = input("\nEnter your choice (C, R or P): ")
    if choice.lower() == "c":
        pi = 3.14
        r = float(input("Enter radius of the circle: "))
        perimeter = 2 * pi * r
        area = pi * r * r
        print("Shape\t\tPerimeter\t\tArea")
        print("*"*50)
        print("Circle\t\t{:.1f}\t\t\t{:.3f}".format(perimeter, area))
    elif choice.lower() == "r":
        w = float(input("Enter length of the rectangle: "))
        h = float(input("Enter width of the rectangle: "))
        perimeter = 2 * (w + h)
        area = w * h
        print("Shape\t\tPerimeter\t\tArea")
        print("*"*50)
        print("Rectangle\t{:.1f}\t\t\t{:.3f}".format(perimeter, area))
    elif choice.lower() == "p":
        s1 = float(input("Enter side1 of the parallelogram: "))
        s2 = float(input("Enter side2 of the parallelogram: "))
        a = int(input("Enter angle between the sides (in degrees): "))
        while (a < 0 or a > 180):
            a = int(input("Enter angle: "))
        perimeter = 2 * (s1 + s2)
        if (a > 0 and a < 90):
            area = (s1 * s2) * math.sin(math.radians(a))
        else:
            area = (s1 * s2) * math.sin(180 - math.radians(a))
        print("Shape\t\tPerimeter\t\tArea")
        print("*"*50)
        print("Parallelogram\t{:.1f}\t\t\t{:.3f}".format(perimeter, area))
    else:
        print("ERROR> Invalid choice: '{}'".format(choice))
    loop = input("Enter another shape?(Y/N): ")
