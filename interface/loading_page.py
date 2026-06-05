# TargetPractice/interface/page_3.py
import turtle
import time

def show_ready_screen():
    turtle.tracer(0)
    turtle.clear()
    turtle.penup()
    turtle.goto(0, 30)
    turtle.pendown()
    turtle.pencolor('silver')
    turtle.write("INITIALIZING RADAR FREQUENCIES...", align="center", font=("times new roman", 20, "bold"))
    turtle.penup()
    
    # Safe macOS window update loop (1.5 seconds)
    for _ in range(15):
        turtle.update()
        time.sleep(0.1)
    turtle.clear()
