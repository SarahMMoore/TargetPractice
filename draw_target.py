# TargetPractice/draw_target.py
import turtle

def square(x, y):
    """Draws a square target boundary and central bullseye at a given coordinate."""
    # Draw outer box border
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.pencolor('silver')
    turtle.pendown()
    
    for _ in range(4):
        turtle.forward(25)
        turtle.left(90)
    turtle.penup()
    
    # Draw central point bullseye (centered inside 25x25 box)
    turtle.goto(x + 12.5, y + 12.5)
    turtle.pencolor('red')
    turtle.dot(6) # Sets specific crisp pixel width for target indicator
    turtle.pencolor('silver')
