# TargetPractice/vectors/x_axis.py
import turtle
from vectors import draw_line

def draw_x():
    turtle.hideturtle()
    turtle.penup()
    # 🎯 CENTERED: Horizontal line drawn exactly across the y = 80 midpoint
    turtle.goto(-275, 80)
    turtle.setheading(0)
    draw_line.draw()
