# TargetPractice/page_3.py
import turtle
import time

def show_ready_screen():
    turtle.clear()
    turtle.penup()
    turtle.goto(0, 50)
    turtle.pendown()
    turtle.pencolor('silver')
    turtle.write("LET'S PLAY!", align="center", font=("times new roman", 25, "bold"))
    turtle.penup()
    
    turtle.update()
    time.sleep(1.5)
    turtle.clear()
