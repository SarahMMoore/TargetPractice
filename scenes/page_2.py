import turtle

# PAGE 2 "How to Play"
def main():    
    line_1()
    line_2()
    line_3()
    line_4()
    line_5()
    pause()

def line_1():
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0,250)
    turtle.pendown()
    turtle.pencolor('silver')
    turtle.write(('TRY TO HIT THE TARGET'),
                 move=False, align="center",
                 font=("times new roman", 20, "bold"))
def line_2():
    turtle.penup()
    turtle.goto(-275,200)
    turtle.pendown()
    turtle.pencolor('silver')
    turtle.write('TO PLAY:',
                 move=False, align="left",
                 font=("times new roman", 20, "normal"))
def line_3():
    turtle.penup()
    turtle.goto(-200,125)
    turtle.pendown()
    turtle.pencolor('silver')
    turtle.write((('~ When prompted, enter the angle and force ')
                + ('\n\tof your projectile.')),
                 move=False, align="left",
                 font=("times new roman", 16, "italic"))    
def line_4():
    turtle.penup()
    turtle.goto(-200,75)
    turtle.pendown()
    turtle.pencolor('silver')
    turtle.write((('~ Hitting anywhere within the square damages ')
                + ('\n\tthe target, but will not destroy it.')),
                 move=False, align="left",
                 font=("times new roman", 16, "italic"))    
def line_5():
    turtle.penup()
    turtle.goto(-200,25)
    turtle.pendown()
    turtle.pencolor('silver')
    turtle.write((('~ To destroy the target, you must hit the ')
                + ('\n\tcenter of the square.')),
                 move=False, align="left",
                 font=("times new roman", 16, "italic"))     
def pause():
    turtle.penup()
    turtle.circle(500)
    turtle.reset()
    turtle.hideturtle()

if __name__ == '__main__': 
    main()
