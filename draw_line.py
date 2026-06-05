import turtle
# Draw line
def main():
    draw()

def draw():
    turtle.pencolor('spring green')
    turtle.pendown()
    for num in range(22):
        turtle.dot()
        turtle.forward(25)
        turtle.dot()
    turtle.penup()

if __name__ == '__main__': 
    main()
