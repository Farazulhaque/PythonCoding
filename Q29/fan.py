from turtle import *
speed(0)
penup()
for x in range(5):
    for i in range(10):
        right(45)
        for j in range(2):
            pendown()
            forward(20)
            left(90)
        right(135)
    for i in range(10):
        left(135)
        for j in range(2):
            pendown()
            forward(20)
            left(90)
        left(45)
    right(75)
done()
