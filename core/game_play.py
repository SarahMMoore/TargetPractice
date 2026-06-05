# core/game_play.py
from graphics import draw_target, crosshairs, scope
from core import config
import turtle

def launch():
    """Initializes key listener event bindings and builds the game loop."""
    turtle.listen()
    
    # Map keyboard actions to controls
    turtle.onkey(increase_angle, "Left")
    turtle.onkey(decrease_angle, "Right")
    turtle.onkey(increase_force, "Up")
    turtle.onkey(decrease_force, "Down")
    turtle.onkey(fire_projectile, "space")
    
    # First frame draw
    render_frame()

def render_frame():
    """Renders the screen graphics, radar grids, and dashboard panel."""
    turtle.tracer(0) # Temporarily turn off animations for instant HUD drawing
    turtle.clear()
    turtle.hideturtle()
    turtle.penup()
    
    # 1. Draw radar systems
    crosshairs.x_axis.setup()
    crosshairs.x_axis.draw_line.draw()
    crosshairs.y_axis.setup()
    crosshairs.y_axis.draw_line.draw()
    scope.draw()
    crosshairs.quadrant.draw()
    draw_target.square()
    
    # 2. 🎛️ Draw Dedicated Bottom HUD Box Layout Panel Bar Line
    turtle.goto(-400, -295) # Aligned with the title menu divider bar
    turtle.setheading(0)
    turtle.pencolor('spring green')
    turtle.pendown()
    turtle.forward(800) 
    turtle.penup()
    
    # 3. Print Live Tuning Data Fields inside lower HUD Space
    turtle.goto(-350, -440) # Centered inside the gameplay HUD box
    hud_text = (
        f"📐 AIM ANGLE: {config.current_angle}° (Use Left/Right Arrows)\n\n"
        f"⚡ LAUNCH FORCE: {config.current_force:.1f} (Use Up/Down Arrows)\n\n"
        f"🚀 TOTAL SHOTS: #{config.shot_count}\n\n"
        f"👉 Press [SPACEBAR] to launch projectile!"
    )
    turtle.write(hud_text, font=("Courier", 12, "bold"))
    
    turtle.update() 
    turtle.tracer(1) 

# 🕹️ Dashboard Key Control Action Functions
def increase_angle():
    if not config.is_fired:
        config.current_angle = (config.current_angle + 5) % 360
        render_frame()

def decrease_angle():
    if not config.is_fired:
        config.current_angle = (config.current_angle - 5) % 360
        render_frame()

def increase_force():
    if not config.is_fired and config.current_force < 10.0:
        config.current_force += 0.5
        render_frame()

def decrease_force():
    if not config.is_fired and config.current_force > 1.0:
        config.current_force -= 0.5
        render_frame()

def fire_projectile():
    if config.is_fired:
        return 
        
    config.is_fired = True
    config.increment_shots()
    render_frame()
    
    # Run fire physics simulation
    FORCE_FACTOR = 30
    distance = config.current_force * FORCE_FACTOR
    
    turtle.goto(0, 0)
    turtle.setheading(config.current_angle)
    turtle.showturtle()
    turtle.pencolor('silver')
    turtle.pendown()
    turtle.forward(distance)
    turtle.dot(6, 'red')
    turtle.penup()
    turtle.hideturtle()
    
    # Evaluate Win/Miss Conditions
    evaluate_outcome()

def evaluate_outcome():
    # Tier 3 Win Condition Check
    if (config.BULLSEYE_X - 5 <= turtle.xcor() <= config.BULLSEYE_X + 5 and 
        config.BULLSEYE_Y - 5 <= turtle.ycor() <= config.BULLSEYE_Y + 5):
        
        turtle.clear()
        turtle.bgcolor('red')
        turtle.pencolor('black')
        turtle.goto(0, 50)
        turtle.write('BULLS-EYE!! YOU WIN!!', align="center", font=("elephant", 22, "bold"))
        turtle.goto(0, 0)
        turtle.write(f'Target destroyed in {config.shot_count} shots!', align="center", font=("elephant", 16, "bold"))
        turtle.bye() 
    else:
        turtle.ontimer(reset_shot, 1500)

def reset_shot():
    config.is_fired = False
    render_frame()
