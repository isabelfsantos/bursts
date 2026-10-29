import turtle
pen = turtle.Turtle()
pen.color("red")
pen.speed(2)
for _ in range(6):
    for _ in range(2):
        pen.circle(100, 60)
        pen.left(120)
    pen.left(60)
pen.hideturtle()
turtle.done()