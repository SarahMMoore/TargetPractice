import turtle
import draw_line

# X-Axis
def main():
    setup()
    draw_line.draw()

def setup():    
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-275,0)                                
    turtle.setheading(0)

if __name__ == '__main__': 
    main()
