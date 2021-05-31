import datetime
dt = datetime.datetime.now().strftime("%c")
t = 0  # for counting triangle
r = 0  # for counting rectangle
c = 0  # for counting circle
# Initially make it true to loop
loop = True
while loop == True:
    choice = int(
        input("1:Triangle, 2:Rectangle, 3: Circle, 4:Count, 5: exit "))
    if choice == 1:
        sides = list(map(float, input("Triangle Side Length: ").split()))
        color = input("Color: ")
        x = sides[0]
        y = sides[1]
        z = sides[2]
        s = (x + y + z) / 2
        area = (s*(s-x)*(s-y)*(s-z)) ** 0.5
        print("Area:", area)
        print("Generate Time:", dt, "Color:", color)
        t += 1
    elif choice == 2:
        sides = list(map(float, input("Rectangle Side Length: ").split()))
        color = input("Color: ")
        l = sides[0]
        b = sides[1]
        area = l * b
        print("Area:", area)
        print("Generate Time:", dt, "Color:", color)
        r += 1
    elif choice == 3:
        rad = float(input("Radius of Circle: "))
        color = input("Color: ")
        area = 3.14 * rad * rad
        print("Area:", area)
        print("Generate Time:", dt, "Color:", color)
        c += 1
    elif choice == 4:
        print("Triangle:", t, ", Rectangle:", r, ", Circle", c)
    elif choice == 5:
        loop = False
