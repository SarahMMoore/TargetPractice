import draw_target
import crosshairs
import scope
import turtle

def main():
    launch()


# Launch projectile
# Loops while angle and force are not equal to winning points 
def launch():
    angle = 0.0
    force = 0.00
    FORCE_FACTOR = 30     # Arbitrary force factor
    PROJECTILE_SPEED = 1  # Projectile's animation speed
    while angle != 66.8 or force != 9.52:
        turtle.clear()
        turtle.hideturtle()
        turtle.penup()
        turtle.bgcolor('black')
        crosshairs.x_axis.setup()
        crosshairs.x_axis.draw_line.draw()
        crosshairs.y_axis.setup()
        crosshairs.y_axis.draw_line.draw()
        scope.draw()
        crosshairs.quadrant.draw()
        draw_target.square()
        
        # Get the angle and force from the user.
        angle = turtle.numinput(('Input'),("Enter the projectile's angle"),
                                minval=0, maxval=360)
        force = turtle.numinput(('Input'),('Enter the launch force (1-10)'),
                                minval=1, maxval=10)
            
        # Calculate the distance.
        distance = force * FORCE_FACTOR
        PLAYER_INPUT = (f'ANGLE: {angle:,.1f}\tFORCE: {force:,.2f}')
        turtle.hideturtle()
        turtle.goto(-250,250)
        turtle.write(PLAYER_INPUT)

        # Center the turtle.
        turtle.goto(0,0)
        turtle.setheading(0)

        # Set the heading.
        turtle.setheading(angle)

        # Launch the projectile
        turtle.showturtle()
        turtle.speed = PROJECTILE_SPEED
        turtle.pencolor('silver')
        turtle.pendown()
        turtle.forward(distance)
        turtle.dot()
        turtle.penup()
        turtle.hideturtle()
        turtle.penup()
        turtle.circle(100)
    
        if (turtle.xcor() <= 112.51 and
            turtle.xcor() >= 112.50 and
            turtle.ycor() <= 262.51 and
            turtle.ycor() >= 262.50):
                turtle.clear()
                turtle.hideturtle()
                turtle.bgcolor('red')
                turtle.pencolor('black')
                turtle.penup()
                turtle.goto(0,100)
                turtle.pendown()
                turtle.write('BULLS-EYE!!',
                             move=False, align="center",
                             font=("elephant", 20, "bold"))  
                turtle.penup()
                turtle.goto(0,50)
                turtle.pendown()
                turtle.write('The target has been destroyed.',
                             move=False, align="center",
                             font=("elephant", 20, "bold"))  
                turtle.penup()
                turtle.goto(0,0)
                turtle.pendown()
                turtle.write('YOU WIN!!',
                             font=("elephant",20,"bold"),align="center")
                turtle.penup()
                for NUM_1 in range(2):
                    turtle.penup()
                    turtle.circle(20)
                    turtle.bgcolor('silver')
                    turtle.circle(20)
                    turtle.bgcolor('red')
                NUM_1 += 1
                turtle.clear()
                turtle.write('Click to exit.',
                             move=False, align="center",
                             font=("elephant", 20, "bold"))
                turtle.exitonclick()
    # Indirect hit          
        elif(turtle.xcor() >= 100 and
             turtle.xcor() <= (100 + 25) and
             turtle.ycor() >= 250 and
             turtle.ycor() <= (250 + 25)):
             turtle.penup()
             turtle.goto(-250,200)
             turtle.pendown()
             turtle.write('You hit the target, but not the center.')
             turtle.penup()
             turtle.goto(-250,150)
             turtle.pendown()
             # Calculate the corrective heading.
             angle_adjust = -angle + 66.8 
             force_adjust = -force + 9.52
             turtle.write(f'Adjust the angle by {angle_adjust:.2f} '
                          + f'degrees\nand the force by {force_adjust:.2f}.')
             turtle.penup()
             turtle.circle(200)
    # Miss
        else:
            turtle.penup()
            turtle.goto(-250,200)
            turtle.pendown()
            turtle.write('You missed the target.')
            turtle.penup()
            turtle.goto(-250, 150)
            turtle.pendown()

            if (angle > 66.8 and force > 9.52):
                    turtle.write(f'Try a slighter angle and use less force.')
                    turtle.penup()
            elif (angle < 66.8 and force < 9.52):
                    turtle.write(f'Try a greater angle and use more force.')
                    turtle.penup()
            elif (angle > 66.8 and force < 9.52):
                    turtle.write(f'Try a slighter angle and use more force.')
                    turtle.penup()
            elif (angle < 66.8 and force > 9.52):
                    turtle.write(f'Try a greater angle and use less force.')
                    turtle.penup()
            elif (angle > 66.8 and force == 9.52):
                    turtle.write(f'Try a slighter angle.')
                    turtle.penup()
            elif (angle < 66.8 and force == 9.52):
                    turtle.write(f'Try a greater angle.')
                    turtle.penup()
            elif (angle == 66.8 and force > 9.52):
                    turtle.write(f'Use less force.')
                    turtle.penup()
            elif (angle == 66.8 and force < 9.52):
                    turtle.write(f'Use more force.')
                    turtle.penup()
            turtle.circle(200)    
        

if __name__ == '__main__':
    main()
