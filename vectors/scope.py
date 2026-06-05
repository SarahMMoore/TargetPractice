# TargetPractice/vectors/scope.py
import turtle

def draw():
    """Draws the tracking circle scope perfectly centered around the y = 80 origin."""
    turtle.penup()
    # 🎯 CENTERED: Placed at (125, 80) so it curves perfectly around the center
    turtle.goto(125, 80)
    turtle.setheading(90)
    turtle.pendown()
    turtle.pencolor('silver')
    turtle.circle(125)
    turtle.penup()
