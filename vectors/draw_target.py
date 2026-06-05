# TargetPractice/vectors/draw_target.py
import turtle

def square(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.pencolor('silver')
    turtle.pendown()
    
    for _ in range(4):
        turtle.forward(25)
        turtle.left(90)
    turtle.penup()
    
    turtle.goto(x + 12.5, y + 12.5)
    turtle.pencolor('red')
    turtle.dot(6)
    turtle.pencolor('silver')
