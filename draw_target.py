import turtle

def main():
    square()

# Draw the target.
def square():
    # Target
    turtle.goto(100, 250)
    turtle.setheading(0)
    turtle.pencolor('silver')
    turtle.pendown()
    TARGET_LINE = 0
    for TARGET_LINE in range (4) :
        turtle.forward(25)
        turtle.left(90)
    TARGET_LINE += 1
    turtle.penup()
    # Draw the bullseye
    turtle.goto(112.5,262.5)
    turtle.pencolor('red')
    turtle.dot()
    turtle.pencolor('silver')

if __name__ == '__main__':
    main()
