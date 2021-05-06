import turtle
skk = turtle.Turtle()

skk.color("blue")
skk.hideturtle()

skk.penup()
skk.goto(-200, 200)
skk.pendown()

# square
for i in range(4):
    skk.forward(400)
    skk.right(90)

# outer circle
skk.penup()
skk.goto(0, -200)
skk.pendown()
skk.circle(200)

# bottom circle
skk.circle(100)

# right circle
skk.penup()
skk.goto(200, 0)
skk.pendown()
skk.left(90)
skk.circle(100)

# left circle
skk.penup()
skk.goto(-200, 0)
skk.pendown()
skk.right(180)
skk.circle(100)

# top circle
skk.penup()
skk.goto(0, 200)
skk.pendown()
skk.right(90)
skk.circle(100)

turtle.done()
