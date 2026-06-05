# TargetPractice/vectors/quadrant.py
import turtle

def draw():
    """Draws the tracking field corner boundaries, perfectly centered in the upper region."""
    turtle.pencolor('spring green')
    
    # 🎯 VERTICALLY CENTERED: Top at 280, Bottom at -120 (leaves 20px padding on both sides)
    coordinates = [
        (275, 280),   # Top Right
        (-275, 280),  # Top Left
        (-275, -120), # Bottom Left
        (275, -120)   # Bottom Right
    ]
    
    for x, y in coordinates:
        turtle.penup()
        turtle.goto(x, y)
        turtle.dot(4)
        mini_crosshairs()

def mini_crosshairs():
    turtle.setheading(0)
    turtle.penup()
    turtle.forward(10)
    turtle.setheading(180)
    turtle.pendown()
    turtle.forward(20)
    turtle.penup()
    turtle.setheading(90)
    turtle.forward(10)
    turtle.setheading(0)
    turtle.forward(10)
    turtle.setheading(270)
    turtle.pendown()
    turtle.forward(20)
    turtle.penup()
