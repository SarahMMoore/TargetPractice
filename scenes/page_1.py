import turtle
from graphics import x_axis
from graphics import y_axis
from graphics import draw_line
from graphics import quadrant
from graphics import scope

# Main
def main():
    line_1()
    x_axis.setup()
    x_axis.draw_line.draw()
    line_2()
    y_axis.setup()
    y_axis.draw_line.draw()
    scope.draw()
    quadrant.draw()
    
# Title line 1    
def line_1():
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-10,15)                                 
    turtle.pendown()
    turtle.pencolor('silver')
    turtle.write('TARGET', move=False, align="right",
                 font=("elephant", 20, "bold"))    
    turtle.penup()

# Title line 2
def line_2():    
    turtle.goto(10,-50)                                 
    turtle.pendown()
    turtle.pencolor('silver')
    turtle.write('PRACTICE', move=False, align="left",
                 font=("elephant", 20, "bold"))  
    turtle.penup()
    
if __name__ == '__main__': 
    main()
