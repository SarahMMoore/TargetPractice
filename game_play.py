# TargetPractice/game_play.py
import turtle
import draw_target
import x_axis
import y_axis
import scope
import quadrant

def launch():
    # Performance optimization: turn off automatic screen rendering
    turtle.tracer(0) 
    
    angle = 0.0
    force = 0.00
    FORCE_FACTOR = 30 
    
    # Active Game Loop
    while angle != 66.8 or force != 9.52:
        turtle.clear()
        turtle.hideturtle()
        turtle.penup()
        turtle.bgcolor('black')
        
        # Safely render all background layers
        x_axis.draw_x()
        y_axis.draw_y()
        scope.draw()
        quadrant.draw()
        draw_target.square()
        
        # Flush the graphics buffer to render instantly
        turtle.update() 
        
        # Prompt user inputs
        angle = turtle.numinput('Input', "Enter the projectile's angle (0-360):", minval=0, maxval=360)
        if angle is None: break # Exit safely if user presses Cancel
        
        force = turtle.numinput('Input', 'Enter the launch force (1-10):', minval=1, maxval=10)
        if force is None: break
        
        # Display chosen tracking variables
        turtle.pencolor('silver')
        turtle.penup()
        turtle.goto(-250, 250)
        turtle.write(f'ANGLE: {angle:.1f}\tFORCE: {force:.2f}', font=("Arial", 12, "bold"))
        
        # Position projectile at origin
        turtle.goto(0, 0)
        turtle.setheading(angle)
        turtle.showturtle()
        turtle.pendown()
        
        # Animate shell vector path
        distance = force * FORCE_FACTOR
        turtle.tracer(1) # Re-enable visibility for the projectile line draw
        turtle.forward(distance)
        turtle.dot(8, 'red') # Visual impact point indicator
        turtle.penup()
        
        # Process hit boundaries
        check_hit_status(turtle.xcor(), turtle.ycor(), angle, force)
        
        # Set tracer back to 0 for background rendering in the next turn
        turtle.tracer(0)

def check_hit_status(hit_x, hit_y, angle, force):
    """Checks coordinate boundaries for bullseyes, target box clips, or misses."""
    # Perfect Direct Center Bullseye
    if 112.4 <= hit_x <= 112.6 and 262.4 <= hit_y <= 262.6:
        turtle.clear()
        turtle.bgcolor('red')
        turtle.pencolor('black')
        
        turtle.goto(0, 100)
        turtle.write('BULLS-EYE!!', align="center", font=("elephant", 20, "bold"))
        turtle.goto(0, 50)
        turtle.write('The target has been destroyed.', align="center", font=("elephant", 20, "bold"))
        turtle.goto(0, 0)
        turtle.write('YOU WIN!!', align="center", font=("elephant", 20, "bold"))
        
        turtle.goto(0, -100)
        turtle.write('Click anywhere to exit.', align="center", font=("elephant", 14, "bold"))
        turtle.exitonclick()
        
    # Indirect Target Box Hit
    elif 100 <= hit_x <= 125 and 250 <= hit_y <= 275:
        turtle.goto(-250, 200)
        turtle.write('You hit the target, but not the center.', font=("Arial", 11, "bold"))
        
        angle_adjust = 66.8 - angle
        force_adjust = 9.52 - force
        turtle.goto(-250, 150)
        turtle.write(f'Adjust angle by: {angle_adjust:.2f}°\nAdjust force by: {force_adjust:.2f}', font=("Arial", 10, "italic"))
        
        turtle.update()
        turtle.numinput("Result", "Indirect Hit! Press OK to adjust values.", minval=0, maxval=0)

    # Miss Status
    else:
        turtle.goto(-250, 200)
        turtle.write('You missed the target.', font=("Arial", 11, "bold"))
        turtle.goto(-250, 150)
        
        if angle > 66.8 and force > 9.52:
            hint = 'Try a slighter angle and use less force.'
        elif angle < 66.8 and force < 9.52:
            hint = 'Try a greater angle and use more force.'
        elif angle > 66.8 and force < 9.52:
            hint = 'Try a slighter angle and use more force.'
        elif angle < 66.8 and force > 9.52:
            hint = 'Try a greater angle and use less force.'
        elif angle == 66.8 and force > 9.52:
            hint = 'Use less force.'
        else:
            hint = 'Use more force.'
            
        turtle.write(hint, font=("Arial", 10, "italic"))
        turtle.update()
        turtle.numinput("Result", "Missed! Press OK to try again.", minval=0, maxval=0)
