# graphics/display.py
import turtle

def main():
    setup()

def setup():
    # Keep the optimized window size at 800x850
    turtle.setup(800, 850)
    turtle.hideturtle()
    turtle.bgcolor('black')
    turtle.speed(0)
    turtle.penup()
    
    # 🎥 CALIBRATED: Shifted viewport up by 25 units to move all graphics down on screen
    # Arguments: (Left, Bottom, Right, Top)
    turtle.setworldcoordinates(-400, -525, 400, 325)
