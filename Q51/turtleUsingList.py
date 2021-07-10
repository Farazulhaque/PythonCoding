import turtle

pen = turtle.Turtle()

l1 = [["F", 50], ["L", 90], ["F", 100], ["R", 90], ["F", 50]]

for i in range(len(l1)):
    if l1[i][0] == "F":
        pen.forward(l1[i][1])
    elif l1[i][0] == "L":
        pen.left(l1[i][1])
    elif l1[i][0] == "R":
        pen.right(l1[i][1])

turtle.done()
