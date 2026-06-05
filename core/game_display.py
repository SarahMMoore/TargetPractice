# TargetPractice/core/game_display.py
import turtle
import random
from core import display, physics
from vectors import x_axis, y_axis, scope, quadrant, draw_target, sweep

# Game Metric State Registries
score = 0
ammo = 5
target_x, target_y = 0, 0
saved_angle, saved_force = 0.0, 0.0
current_string = ""
input_mode = "angle"
feedback_msg = "SYSTEM INITIALIZED. SCANNING RADAR GRID SENSORS..."
feedback_color = "spring green"

def launch():
    global score, input_mode, current_string, feedback_msg, feedback_color, ammo
    score, ammo = 0, 5
    input_mode = "angle"
    current_string = ""
    feedback_msg = "SYSTEM INITIALIZED. SCANNING RADAR GRID SENSORS..."
    feedback_color = "spring green"
    
    spawn_new_target()
    turtle.listen()
    bind_keys()
    refresh_deck()

def spawn_new_target():
    global target_x, target_y
    target_x = random.randint(-180, 180)
    target_y = random.randint(0, 160)  
    physics.calculate_target_solution(target_x, target_y)

def refresh_deck():
    turtle.tracer(0)
    turtle.clear()
    turtle.hideturtle()
    turtle.penup()
    turtle.bgcolor('#0b130e')
    
    x_axis.draw_x()
    y_axis.draw_y()
    scope.draw()
    quadrant.draw()
    draw_target.square(target_x, target_y)
    
    physics.draw_historical_trails()
    display.draw_dashboard_hud(score, ammo, input_mode, current_string, feedback_msg, feedback_color)
    turtle.update()

def draw_debrief_exit_screen():
    """🎯 FIXED: Renders final summary screen and waits for user click to close."""
    turtle.tracer(0)
    turtle.clear()
    turtle.hideturtle()
    turtle.bgcolor('#070b09') # Deep charcoal green background layout
    
    # Render stylized tactical grid borders
    turtle.pencolor('#00ff66')
    turtle.penup()
    turtle.goto(-280, 260)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(560)
        turtle.right(90)
    turtle.penup()
    
    # Print Final Tactical Performance Log Results
    turtle.goto(0, 80)
    turtle.write("📟 TELEMETRY FEED TERMINATED", align="center", font=("Courier", 18, "bold"))
    
    turtle.goto(0, 20)
    turtle.pencolor('white')
    turtle.write("GOODBYE OFFICER. OPERATIONAL CHANNELS CLOSING.", align="center", font=("times new roman", 15, "bold"))
    
    turtle.goto(0, -40)
    turtle.pencolor('#00ff66')
    # Displays the accumulated matching score matrix calculation
    turtle.write(f"🏆 FINAL EFFICIENCY TOTAL: {score} XP", align="center", font=("Courier", 14, "bold"))
    
    turtle.goto(0, -140)
    turtle.pencolor('silver')
    # 🎯 FIXED: Message informing the player that click-to-exit retention is active
    turtle.write("Click anywhere inside this screen to safely exit.", align="center", font=("Arial", 11, "italic"))
    
    turtle.update()
    # 🎯 FIXED: Locks window loop open permanently until user physically triggers a click event
    turtle.exitonclick()

# --- KEYBOARD TERMINAL STROKE HANDLERS ---

def process_key(char):
    global current_string
    if input_mode in ["angle", "force"]:
        if char.isdigit() or (char == '.' and '.' not in current_string):
            if len(current_string) < 6:
                current_string += char
                refresh_deck()
    elif input_mode in ["victory", "gameover"] and char.lower() in ['y', 'n', 'c']:
        current_string = char.upper()
        refresh_deck()

def trigger_backspace():
    global current_string
    if input_mode in ["angle", "force", "victory", "gameover"] and len(current_string) > 0:
        current_string = current_string[:-1]
        refresh_deck()

def trigger_enter():
    global current_string, input_mode, saved_angle, saved_force, feedback_msg, feedback_color, score, ammo
    if current_string == "": return
    
    if input_mode == "angle":
        try:
            val = float(current_string)
            if 0 <= val <= 360:
                saved_angle = val
                input_mode = "force"
                feedback_msg = f"AZIMUTH SECURED AT {saved_angle:.1f}°. COMPUTE RANGE FACTOR..."
                feedback_color = "spring green"
            else:
                feedback_msg = "OUT OF RANGE ALERT. INPUT HEADING MUST BE 0-360 DEGREES."
                feedback_color = "red"
        except ValueError: pass
        current_string = ""
        
    elif input_mode == "force":
        try:
            val = float(current_string)
            if 1 <= val <= 10:
                saved_force = val
                current_string = ""
                ammo -= 1
                is_hit, feedback_msg, feedback_color, score_bonus = physics.simulate_shot(saved_angle, saved_force, target_x, target_y)
                score += score_bonus
                input_mode = "victory" if is_hit else "wait"
            else:
                feedback_msg = "OUT OF VELOCITY BOUNDS. VELOCITY FACTOR MUST BE 1-10 VALUE."
                feedback_color = "red"
        except ValueError: pass
        current_string = ""
        
    elif input_mode in ["victory", "gameover"]:
        choice = current_string.upper()
        current_string = ""
        if choice == "C" and score >= 100:
            score -= 100
            ammo = 5
            input_mode = "angle"
            feedback_msg = "⚡ SUPPLY DEPLOYED! 5 ROUNDS PURPOSED. POSITION RETENTION ACTIVE."
            feedback_color = "spring green"
        elif choice == "Y":
            input_mode = "angle"
            feedback_msg = "DEPLOYING INCOMING RADAR PARALLEL VECTOR GRID MATRIX..."
            feedback_color = "spring green"
            spawn_new_target()
        else:
            draw_debrief_exit_screen()
            return
            
    refresh_deck()

def trigger_space():
    global input_mode, feedback_msg, feedback_color
    if input_mode == "wait":
        if ammo <= 0:
            input_mode = "gameover"
            feedback_msg = "🚨 OUT OF AMMO! Restart [Y], Close [N], or Buy 5 rounds for 100 XP [C]:"
            feedback_color = "red"
            refresh_deck()
            return
        input_mode = "angle"
        feedback_msg = "TELEMETRY RESET. SCANNING RADAR GRID SENSORS..."
        feedback_color = "spring green"
        refresh_deck()

def bind_keys():
    for num in "0123456789.ynYNcC":
        turtle.onkey(lambda n=num: process_key(n), num)
    turtle.onkey(trigger_backspace, "BackSpace")
    turtle.onkey(trigger_enter, "Return")
    turtle.onkey(trigger_space, "space")
