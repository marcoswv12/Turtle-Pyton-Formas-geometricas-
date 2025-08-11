import turtle


t = turtle.Turtle ()
t.pencolor("red")
t.pensize(5)
t.forward(100) 
t.left(90)
t.forward(100)
t.right(90)
t.backward(100)
t.right(90)
t.forward(100)


t.penup()
t.goto(200,0)
t.pendown()
t.pensize(5)
t.pencolor("blue")
t.left(90)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)

t.penup()
t.goto(-200,73)
t.pendown()
t.pensize(5)
t.pencolor("yellow")
t.circle(60)

t.penup()
t.goto(10, -50)
t.pendown()
t.pencolor("green")


for _ in range(6):
    t.forward(70)
    t.left(60)






