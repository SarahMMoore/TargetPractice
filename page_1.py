# TargetPractice/page_1.py
import turtle
import x_axis
import y_axis
import quadrant
import scope

def draw_intro_grid():
    turtle.clear()
    
    # Title Text Line 1
    turtle.penup()
    turtle.goto(-10, 15)
    turtle.pendown()
    turtle.pencolor('silver')
    turtle.write('TARGET', align="right", font=("elephant", 20, "bold"))
    
    # Title Text Line 2
    turtle.penup()
    turtle.goto(10, -50)
    turtle.pendown()
    turtle.write('PRACTICE', align="left", font=("elephant", 20, "bold"))
    turtle.penup()
    
    # Run structural drawings directly
    x_axis.draw_x()
    y_axis.draw_y()
    scope.draw()
    quadrant.draw()
