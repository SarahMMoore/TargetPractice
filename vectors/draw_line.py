# TargetPractice/vectors/draw_line.py
import turtle

def draw():
    """Draws a perfectly uniform sequence of tracking grid dots across the axis."""
    turtle.pencolor('spring green')
    # Keep the pen up during travel so it never accidentally draws a solid line
    turtle.penup() 
    
    for _ in range(23):
        turtle.dot(4) # Draws a crisp grid coordinate point
        turtle.forward(25)
