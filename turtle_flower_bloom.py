import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.setup(width=800, height=800)
s.bgcolor("#262626")
t.speed(100)
t.penup()
t.goto(160, -160)
t.pendown()
col = ('#ED7864', '#6E544F', '#592F2F', '#6E382E')
for n in range(5):
    t.pencolor(col[n % len(col)])
    for x in range (8):
        t.speed(x+10)
        for i in range(2):
            t.pensize(2)
            t.circle(80+n*20, 90)
            t.lt(90)
        t.lt(45)
t.hideturtle()
turtle.done()