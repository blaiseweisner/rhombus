import turtle

screen = turtle.Screen()
turtle.screensize(500, 500)
t = turtle.Turtle()
t.speed(0)
screen.bgcolor('yellow')

t.goto(0,0)
t.pendown()
t.fillcolor('cyan')
t.begin_fill()
t.setheading(135)
t.forward(90)
t.left(90)
t.forward(90)
t.left(90)
t.forward(90)
t.left(90)
t.forward(90)
t.end_fill()

t.fillcolor('brown')
t.begin_fill()
t.forward(90)
t.right(90)
t.forward(90)
t.right(90)
t.forward(90)
t.right(90)
t.forward(90)
t.end_fill()













turtle.done()