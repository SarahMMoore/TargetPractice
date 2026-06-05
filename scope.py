import turtle

def main():
    draw()

# Draw scope
def draw():
    turtle.goto(150,0)                                     
    turtle.setheading(90)
    turtle.pendown()
    turtle.pencolor('silver')
    turtle.circle(150)
    turtle.penup()

if __name__ == '__main__':
    main()
