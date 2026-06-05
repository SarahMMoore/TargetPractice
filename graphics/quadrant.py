import turtle

def main():
    draw()

# Draw corners    
def draw():
    turtle.goto(275,275)
    turtle.pencolor('spring green')
    turtle.dot()
    mini_crosshairs()
    turtle.goto(-275,275)                                     
    turtle.dot()
    mini_crosshairs()
    turtle.goto(-275,-275)                                     
    turtle.dot()
    mini_crosshairs()
    turtle.goto(275,-275)                                     
    turtle.dot()
    mini_crosshairs()

# Draw mini crosshairs
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
    
if __name__ == '__main__': 
    main()
