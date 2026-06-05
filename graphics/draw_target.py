# graphics/draw_target.py
import turtle
from core import config  # Import encapsulated game state

def main():
    square()

def square():
    # Use randomized coordinates from core/config.py
    turtle.goto(config.TARGET_X, config.TARGET_Y)
    turtle.setheading(0)
    turtle.pencolor('silver')
    turtle.pendown()
    
    for _ in range(4):
        turtle.forward(config.TARGET_SIZE)
        turtle.left(90)
        
    turtle.penup()
    
    # Draw the dynamic bullseye exactly in the center of the randomized target
    turtle.goto(config.BULLSEYE_X, config.BULLSEYE_Y)
    turtle.pencolor('red')
    turtle.dot()
    turtle.pencolor('silver')