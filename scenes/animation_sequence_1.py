import turtle

# Main
def main():
    print_title_line_1()
    draw_x_axis()
    print_title_line_2()
    draw_y_axis()
    quadrants()
    
# Title line 1    
def print_title_line_1():
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-10,15)                                 
    turtle.pendown()
    turtle.pencolor('silver')
    turtle.write('TARGET', move=False, align="right",
                 font=("elephant", 20, "bold"))    
    turtle.penup()

# Title line 2
def print_title_line_2():    
    turtle.goto(10,-50)                                 
    turtle.pendown()
    turtle.pencolor('silver')
    turtle.write('PRACTICE', move=False, align="left",
                 font=("elephant", 20, "bold"))  
    turtle.penup()
    
if __name__ == '__main__': 
    main()
