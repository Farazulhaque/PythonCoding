print("1. Rectangle")
print("2. Circle")
print("3. Square")
print("4. Triangle")
choice = input("Enter the first letter of the geometric shape: ")
if choice.lower() == 'r':
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    area = l * b
    print("Area =", area)

elif choice.lower() == 'c':
    r = float(input("Enter radius: "))
    area = 3.14 * r * r
    print("Area =", area)

elif choice.lower() == 's':
    s = float(input("Enter side: "))
    area = s ** 2
    print("Area =", area)

elif choice.lower() == 't':
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    area = 1/2 * b * h
    print("Area =", area)

else:
    print("Invalid Input")

if choice.lower() in ['s', 'r']:
    shape = input(
        "Do you want to draw the shape in the output screen? [Y/n]")
    if shape.lower() == 'y':
        if choice.lower() == 's':
            for row in range(5):
                for col in range(5):
                    print("*", end=" ")
                print()

        if choice.lower() == 'r':
            for i in range(5):
                for j in range(10):
                    print('*', end='  ')
                print()
