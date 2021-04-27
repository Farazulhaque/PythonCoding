import turtle
import random

x = turtle.Turtle()
x.speed(0)

# select random color from this list
color = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
x.color(random.choice(color))

x.hideturtle()
x.penup()
x.goto(0, 0)
x.pendown()

x.begin_fill()
x.left(30)
for i in range(3):
    x.forward(8)
    x.left(120)
    x.forward(8)
x.end_fill()

x.penup()
x.goto(-100, 100)
x.pendown()

x.begin_fill()
for i in range(3):
    x.forward(8)
    x.left(120)
    x.forward(8)
x.end_fill()

x.penup()
x.goto(100, 100)
x.pendown()

x.begin_fill()
for i in range(3):
    x.forward(8)
    x.left(120)
    x.forward(8)
x.end_fill()

turtle.done()
