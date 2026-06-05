import turtle
import draw_line

# Y-Axis
def main():
    setup()
    draw_line.draw()

def setup():
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0,275)                                
    turtle.setheading(270)

if __name__ == '__main__': 
    main()
