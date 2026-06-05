import turtle

# DISPLAY SETUP
def main():
    setup()

def setup(): 
    turtle.setup(600,600)
    turtle.hideturtle()
    turtle.bgcolor('black')
    turtle.speed = 10
    turtle.penup()    

if __name__ == '__main__': 
    main()
