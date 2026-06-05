# graphics/y_axis.py
import turtle
from . import draw_line  # 🌟 FIXED: Added the dot here so it finds it inside graphics

# Y-Axis
def main():
    setup()
    draw_line.draw()
    # Safe lift-up so it never leaves a stray line
    turtle.penup() 

def setup():
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0, 275)
    turtle.setheading(270)

if __name__ == '__main__':
    main()