# TargetPractice/game_play.py
import turtle
import random
import draw_target
import x_axis
import y_axis
import scope
import quadrant
import math

# Global state tracker to safely handle screen pausing without freezing the app window
waiting_for_next_turn = False

def launch():
    global waiting_for_next_turn
    turtle.tracer(0) 
    FORCE_FACTOR = 30 
    
    # Generate random target positions
    target_x = random.randint(-200, 200)
    target_y = random.randint(-200, 200)
    
    bullseye_x = target_x + 12.5
    bullseye_y = target_y + 12.5
    
    # Configure window event listeners for key taps
    turtle.listen()
    
    def advance_turn():
        global waiting_for_next_turn
        waiting_for_next_turn = False

    # Bind the Spacebar key to advance past target misses cleanly
    turtle.onkey(advance_turn, "space")
    
    while True:
        turtle.clear()
        # FIX 1: Explicitly make sure the turtle is hidden at the start of the frame
        turtle.hideturtle()
        turtle.penup()
        turtle.bgcolor('black')
        
        # Render clean background vectors
        x_axis.draw_x()
        y_axis.draw_y()
        scope.draw()
        quadrant.draw()
        draw_target.square(target_x, target_y)
        turtle.update() 
        
        # Capture input values safely
        angle = turtle.numinput('Aiming Control', "Enter your launch angle (0-360):", minval=0, maxval=360)
        if angle is None: break
        
        force = turtle.numinput('Aiming Control', 'Enter launch force (1-10):', minval=1, maxval=10)
        if force is None: break
        
        # Render tracking stat string overlay
        turtle.pencolor('silver')
        turtle.penup()
        turtle.goto(-250, 250)
        turtle.write(f'ANGLE: {angle:.1f}\tFORCE: {force:.2f}', font=("Arial", 12, "bold"))
        
        # Position projectile at origin
        turtle.goto(0, 0)
        turtle.setheading(angle)
        
        # FIX 2: Removed turtle.showturtle() so the arrow never becomes visible
        turtle.hideturtle() 
        turtle.pendown()
        
        # Trace active line path across the screen
        distance = force * FORCE_FACTOR
        turtle.tracer(1) 
        turtle.forward(distance)
        turtle.dot(8, 'red') 
        turtle.penup()
        turtle.hideturtle() # Extra safety cleanup
        
        hit_x, hit_y = turtle.xcor(), turtle.ycor()
        
        # Passing all required arguments into the hit calculator
        is_won = check_hit_status(hit_x, hit_y, target_x, target_y, bullseye_x, bullseye_y, angle, force)
        if is_won:
            break
            
        # Freeze screen loop and wait for spacebar key response from user
        waiting_for_next_turn = True
        turtle.goto(-275, 100) # Patched to -275 to fix line overlap alignment text bug
        turtle.pencolor('yellow')
        turtle.write("Press [SPACEBAR] to clear and try again.", font=("Arial", 11, "bold"))
        turtle.update()
        
        turtle.tracer(0)
        while waiting_for_next_turn:
            turtle.update()

def check_hit_status(hit_x, hit_y, t_x, t_y, b_x, b_y, current_angle, current_force):
    """Processes precision checking loops with smart mathematical guidance paths."""
    # 1. Bullseye Center Area Match Check
    if (b_x - 2.5) <= hit_x <= (b_x + 2.5) and (b_y - 2.5) <= hit_y <= (b_y + 2.5):
        turtle.clear()
        turtle.bgcolor('red')
        turtle.pencolor('black')
        
        turtle.goto(0, 100)
        turtle.write('BULLS-EYE!!', align="center", font=("elephant", 20, "bold"))
        turtle.goto(0, 50)
        turtle.write('The random target has been destroyed.', align="center", font=("elephant", 20, "bold"))
        turtle.goto(0, 0)
        turtle.write('YOU WIN!!', align="center", font=("elephant", 20, "bold"))
        
        turtle.goto(0, -100)
        turtle.write('Click anywhere to exit.', align="center", font=("elephant", 14, "bold"))
        turtle.exitonclick()
        return True
        
    # 2. Outer Square Boundaries Box Target Clip Check
    elif t_x <= hit_x <= (t_x + 25) and t_y <= hit_y <= (t_y + 25):
        target_angle = math.degrees(math.atan2(b_y, b_x)) % 360
        target_force = math.sqrt(b_x**2 + b_y**2) / 30.0
        
        angle_adjust = target_angle - current_angle
        force_adjust = target_force - current_force
        
        turtle.goto(-250, 200)
        turtle.write('You hit the target, but missed the center bullseye.', font=("Arial", 11, "bold"))
        turtle.goto(-250, 150)
        turtle.write(f'Adjust angle by: {angle_adjust:.1f}°\nAdjust force by: {force_adjust:.2f}', font=("Arial", 10, "italic"))
        return False

    # 3. Miss Condition
    else:
        turtle.goto(-250, 200)
        turtle.write('You missed the target entirely.', font=("Arial", 11, "bold"))
        
        target_angle = math.degrees(math.atan2(b_y, b_x)) % 360
        target_force = math.sqrt(b_x**2 + b_y**2) / 30.0
        
        hint_angle = "greater" if current_angle < target_angle else "slighter"
        hint_force = "more" if current_force < target_force else "less"
        
        turtle.goto(-250, 150)
        turtle.write(f'Hint: Try a {hint_angle} angle and {hint_force} force.', font=("Arial", 10, "italic"))
        return False
