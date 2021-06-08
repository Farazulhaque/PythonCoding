import turtle
t = turtle.Turtle()


def setPos(x, y):
    t.penup()  # picks up the turtle's pen so that it does not draw
    t.setpos(x, y)  # sets the position
    t.pendown()  # puts down the turtle's pen
    t.width(3)  # sets the width of turtle


def hexagon():
    # sets the color of the turtle, hence it creates the border
    t.pencolor("blue")
    t.fillcolor("yellow")  # sets the background color of the figure
    t.begin_fill()  # this will start filling colors
    for i in range(6):
        t.forward(50)
        t.right(60)
    t.end_fill()  # this will end filling colors


def circle():
    # sets the color of the turtle, hence it creates the border
    t.pencolor("red")
    t.fillcolor("blue")  # sets the background color of the figure
    t.begin_fill()  # this will start filling colors
    t.circle(45)
    t.end_fill()  # this will end filling colors


def square():
    # sets the color of the turtle, hence it creates the border
    t.pencolor("black")
    t.fillcolor("red")  # sets the background color of the figure
    t.begin_fill()  # this will start filling colors
    for i in range(4):
        t.forward(90)
        t.right(90)
    t.end_fill()  # this will end filling colors


# initial position of the turtle
x, y = -300.00, 300.00

for i in range(3):
    setPos(x, y)
    hexagon()
    x, y = x+130.00, y-90.00  # initializing new position values
    setPos(x, y)
    circle()
    x, y = x+60.00, y+90.00  # initializing new position values
    setPos(x, y)
    square()
    x, y = x-90.00, y-110.00  # initializing new position values

t.hideturtle()  # hides the turtle from the screen
turtle.done()
