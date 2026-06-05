# TargetPractice/vectors/sweep.py
import turtle
import time

def run_radar_scan():
    """Simulates a highly realistic military-grade sweeping radar scanner beam."""
    # Temporarily speed up drawing calculations to render the sweep line smoothly
    turtle.tracer(0)
    
    # Create a secondary custom turtle so we don't accidentally move your main shot pen
    scanner = turtle.Turtle()
    scanner.hideturtle()
    scanner.speed(0)
    
    # Run two full 360-degree high-tech sweeps around our centralized origin (0, 80)
    for angle in range(0, 720, 12):
        # 1. Clear out the previous frame's sweeping beam line instantly
        scanner.clear()
        
        # 2. Position scanner pen at your new true region midpoint center coordinates
        scanner.penup()
        scanner.goto(0, 80)
        scanner.setheading(angle)
        
        # 3. Project the beam outward matching the exact 125 radius of your scope circle
        scanner.pendown()
        scanner.pencolor('#105e26') # Classic deep phosphor radar green color tint
        scanner.pensize(2)
        scanner.forward(125)
        
        # 4. Flash a bright tracking ping dot at the tip perimeter edge
        scanner.dot(6, '#00ff66')
        
        # Flush graphics to screen buffer and add a micro-delay for speed regulation
        turtle.update()
        time.sleep(0.02)
        
    # Completely erase the laser tracer beam once scanning is finished
    scanner.clear()
    turtle.update()
