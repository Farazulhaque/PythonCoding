# import turtle
# snappy = turtle.Turtle()


# def drawL(t, short, long):
#     t.forward(short)
#     t.backward(short)
#     t.left(90)
#     t.forward(long)
#     t.backward(long)


# drawL(snappy, 50, 100)

# turtle.done()

import turtle
snappy = turtle.Turtle()


def justLs(pen, side, num, angle):
    for i in range(num):
        pen.forward(side)
        pen.backward(side)
        pen.left(90)
        pen.forward(side*2)
        pen.backward(side*2)
        pen.right(90)
        pen.left(angle)


justLs(snappy, 35, 12, 25)

turtle.done()
