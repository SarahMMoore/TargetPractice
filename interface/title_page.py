# TargetPractice/interface/title_page.py
import turtle
import time
from vectors import x_axis, y_axis, scope, quadrant

def show_tutorial():
    """Combines the radar graphics grid, title headers, and tutorial text into a single split screen."""
    turtle.tracer(0)
    turtle.clear()
    turtle.bgcolor('#0b130e') # Dark tactical radar cockpit theme
    
    # 1. RENDER TOP RADAR GRAPHICS FIELD
    x_axis.draw_x()
    y_axis.draw_y()
    scope.draw()
    quadrant.draw()
    
    # 🎯 2. PERFECT CORNER OFFSET TITLE MATCH (Adjusted relative to y = 80 center)
    turtle.pencolor('silver')
    # "TARGET" - Right-aligned to the left of the vertical axis line, sitting just above y=80
    write_text(-15, 95, "TARGET", "elephant", 20, "bold", "right")
    
    # "PRACTICE" - Left-aligned to the right of the vertical axis line, dropped into lower right quadrant
    write_text(15, 35, "PRACTICE", "elephant", 20, "bold", "left")
    
    # 3. DRAW H.U.D. COCKPIT DIVIDER LINE
    turtle.penup()
    turtle.goto(-300, -140)
    turtle.pencolor('#00ff66')
    turtle.pensize(2)
    turtle.pendown()
    turtle.goto(300, -140)
    turtle.penup()
    turtle.pensize(1)
    
    # 4. RENDER TUTORIAL INSTRUCTIONS INSIDE LOWER PANEL DECK
    turtle.pencolor('white')
    write_text(-270, -170, "📡 SYSTEM TUTORIAL MODE / HOW TO ENGAGE TARGETS:", "Courier", 11, "bold", "left")
    
    turtle.pencolor('silver')
    write_text(-250, -200, "~ Input Launch Azimuth (Compass Angle heading: 0-360°)", "Courier", 10, "normal", "left")
    write_text(-250, -225, "~ Input Terminal Velocity (Thrust Power Factor: 1-10)", "Courier", 10, "normal", "left")
    write_text(-250, -250, "~ Bullseye = Vaporized Target | Outer Square Clip = +50 XP Proximity bonus", "Courier", 10, "normal", "left")
    write_text(-250, -275, "~ Missed trajectory trails are saved to your screen matrix memory banks", "Courier", 10, "normal", "left")
    
    # Safe macOS window update loop (6 seconds display hold)
    for _ in range(60):
        turtle.update()
        time.sleep(0.1)
    turtle.clear()

def write_text(x, y, text, font_name, size, style, alignment):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(text, align=alignment, font=(font_name, size, style))
    turtle.penup()
