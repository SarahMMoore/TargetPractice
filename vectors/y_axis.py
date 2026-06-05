# TargetPractice/vectors/y_axis.py
import turtle

def draw_y():
    """Draws the vertical axis line, stopping perfectly at our new boundaries."""
    turtle.hideturtle()
    turtle.pencolor('spring green')
    turtle.penup()
    
    # Start at the new top boundary
    turtle.goto(0, 280)
    turtle.setheading(270)
    
    # 🎯 CENTERED: Draws exactly 17 dots from y=280 down to y=-120
    for _ in range(17):
        turtle.dot(4)
        turtle.forward(25)
