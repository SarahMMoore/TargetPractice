# scenes/title_animations.py
from scenes import page_1
from core import game_play
import turtle

def start_menu():
    """Draws the title menu and perfectly centers the instructions in the lower zone."""
    turtle.tracer(0) # Render frame instantly
    turtle.clear()
    turtle.hideturtle()
    turtle.penup()
    
    # 1. Render core legacy Title elements from page_1 (shifted down automatically)
    page_1.line_1() 
    page_1.x_axis.setup()
    page_1.x_axis.draw_line.draw()
    page_1.line_2() 
    page_1.y_axis.setup()
    page_1.y_axis.draw_line.draw()
    page_1.scope.draw()
    page_1.quadrant.draw()
    
    # 2. 🟩 Draw the separating line cleanly below the lowest crosshairs
    turtle.goto(-400, -295)
    turtle.setheading(0)
    turtle.pencolor('spring green')
    turtle.pendown()
    turtle.forward(800)
    turtle.penup()
    
    # 3. 📄 Position and center the instructions text blocks in the new balanced zone
    turtle.goto(0, -420) # Balanced coordinate position
    turtle.pencolor('silver')
    instructions = (
        "--- GAME MANUAL & INSTRUCTIONS ---\n\n"
        "🎮 Use [LEFT] / [RIGHT] Arrow Keys to tune your AIM ANGLE\n"
        "⚡ Use [UP] / [DOWN] Arrow Keys to adjust your LAUNCH FORCE\n"
        "🚀 Press the [SPACEBAR] to fire your projectile at the field\n"
        "🎯 Mission: Land directly on the red center bullseye to win!\n\n"
        "👉 PRESS [ENTER] TO UNLOCK RADAR CONTROLS"
    )
    turtle.write(instructions, align="center", font=("Courier", 11, "bold"))
    
    turtle.update() 
    turtle.tracer(1) 
    
    # 4. Bind the [ENTER] key listener
    turtle.listen()
    turtle.onkey(initialize_radar_screen, "Return")

def initialize_radar_screen():
    turtle.onkey(None, "Return") 
    turtle.clear()
    turtle.bgcolor('black')
    turtle.hideturtle()
    
    # Position loading texts nicely within the adjusted world coordinates
    turtle.goto(0, 40)
    turtle.pencolor('red')
    turtle.write("⚠️ WARNING: CALIBRATING WEAPON SYSTEMS...", align="center", font=("Courier", 16, "bold"))
    
    turtle.goto(0, -30)
    turtle.pencolor('spring green')
    turtle.write("INITIALIZING RADAR SCANNER ARRAY...", align="center", font=("Courier", 14, "normal"))
    
    turtle.goto(0, -80)
    turtle.pencolor('silver')
    turtle.write("Please stand by...", align="center", font=("Courier", 12, "italic"))
    
    turtle.update()
    turtle.ontimer(game_play.launch, 4000)

if __name__ == '__main__':
    start_menu()
