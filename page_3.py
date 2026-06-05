import turtle

# Main
def main():    
    line()
    pause()

def line():
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0,50)                               
    turtle.pendown()
    turtle.pencolor('silver')
    turtle.write("LET'S PLAY!",
                 move=False, align="center",
                 font=("times new roman", 25, "bold"))
def pause():
    turtle.penup()
    turtle.circle(200)                                  
    turtle.reset()
    turtle.hideturtle()

if __name__ == '__main__': 
    main()
