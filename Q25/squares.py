from turtle import *
import turtle
from random import randint

print("This program draws squares of many colors\n")
end = False
while not end:
    try:
        num = int(input("Enter the number of squares to draw: "))
        end = True
    except ValueError:
        print("The number must be integer and atleast 1.")
        print("Please try again.\n")

side = turtle.Turtle()
side.hideturtle()
screen = Screen()
screen.colormode(255)
for i in range(num):
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    side.penup()
    side.goto(0, 0)
    side.pendown()

    side.begin_fill()
    side.fillcolor((r, g, b))
    for j in range(4):
        side.forward(100)
        side.left(90)
    side.end_fill()
    side.left(40)

turtle.done()
