# TargetPractice/game_play.py
import turtle
import random
import draw_target
import x_axis
import y_axis
import scope
import quadrant
import math

# Global Game Engine States
score = 0
ammo = 5
target_x = 0
target_y = 0

# True Polar Telemetry Target Solutions
target_bearing = 0.0    
target_range = 0.0      

# SHOT HISTORY MEMORY TRACKING VARIABLES
last_angle = "NONE"
last_force = "NONE"

# Interactive Input Capture States
input_mode = "angle"  # Can be "angle", "force", "wait", "victory", or "gameover"
current_string = ""   
saved_angle = 0.0
saved_force = 0.0
feedback_msg = "SYSTEM INITIALIZED. SCANNING RADAR GRID SENSORS..."
feedback_color = "spring green"

def init_new_polar_target():
    """Generates a random target and extracts true Polar Coordinate Telemetry Solutions."""
    global target_x, target_y, target_bearing, target_range, last_angle, last_force, ammo
    
    target_x = random.randint(-220, 220)
    target_y = random.randint(-60, 220) 
    
    raw_radians = math.atan2(target_y, target_x)
    target_bearing = math.degrees(raw_radians) % 360
    target_range = math.sqrt(target_x**2 + target_y**2)
    
    # Reset tracking metrics for a fresh match
    last_angle = "NONE"
    last_force = "NONE"
    ammo = 5

def draw_dashboard_deck():
    """Draws a tactical radar fire control telemetry display deck panel overlay."""
    turtle.tracer(0)
    
    # 1. Dashboard Divider Line
    turtle.penup()
    turtle.goto(-300, -140)
    turtle.pencolor('#00ff66') 
    turtle.pensize(2)
    turtle.pendown()
    turtle.goto(300, -140)
    turtle.penup()
    turtle.pensize(1)
    
    # 2. Score Widget
    turtle.goto(-270, -165)
    turtle.pencolor('white')
    turtle.write(f"📊 SYSTEM SCORE: {score} XP", font=("Courier", 11, "bold"))
    
    # 3. Ammo Clip Indicator
    turtle.goto(80, -165)
    ammo_blocks = "█" * ammo
    empty_blocks = "░" * (5 - ammo)
    turtle.write(f"🔋 ORDNANCE CAPACITY: [{ammo_blocks}{empty_blocks}]", font=("Courier", 11, "bold"))
    
    # 4. PERSISTENT TELEMETRY SHOT HISTORY READOUT
    turtle.goto(-270, -195)
    turtle.pencolor('silver')
    if last_angle == "NONE":
        history_text = "📟 SHOT TELEMETRY HISTORY >> [ NO PRIOR ORDNANCE DEPLOYED ]"
    else:
        history_text = f"📟 LAST SHOT RECORDED  >> ANGLE: {last_angle:.1f}°  |  FORCE: {last_force:.2f} Mach"
    turtle.write(history_text, font=("Courier", 10, "bold"))
    
    # 5. Command Line Prompt (Handles victory text logic choices natively)
    turtle.goto(-270, -225)
    turtle.pencolor('#00ff66')
    if input_mode == "angle":
        prompt_text = f"⚙️ RADAR DESK >> Input Launch Azimuth (Bearing 0-360°): {current_string}_"
    elif input_mode == "force":
        prompt_text = f"⚙️ RADAR DESK >> Input Terminal Velocity (Thrust Range 1-10): {current_string}_"
    elif input_mode == "victory":
        prompt_text = "🎯 TARGET SOLVED! Engage another target coordinate blueprint? [Y/N]: " + current_string + "_"
    elif input_mode == "gameover":
        prompt_text = "🚨 MISSION DEFEAT! Out of ammunition. Try again? [Y/N]: " + current_string + "_"
    else:
        prompt_text = "📡 VECTOR LOCKED >> Press [SPACEBAR] to recalibrate telemetry lines."
    turtle.write(prompt_text, font=("Courier", 10, "bold"))
    
    # 6. Live Telemetry Target Feed Output Row
    turtle.goto(-270, -255)
    turtle.pencolor(feedback_color)
    turtle.write(f">> {feedback_msg}", font=("Courier", 10, "bold"))

def refresh_screen():
    """Clears and renders the structural tracking field components."""
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
    
    draw_dashboard_deck()
    turtle.update()

def launch():
    """Main radar engine runner loop. Installs direct system key capturing hooks."""
    global input_mode, current_string, saved_angle, saved_force, score, feedback_msg, feedback_color
    score = 0 # Fresh global score initialize
    input_mode = "angle"
    current_string = ""
    feedback_msg = "SYSTEM INITIALIZED. SCANNING RADAR GRID SENSORS..."
    feedback_color = "spring green"
    
    init_new_polar_target()
    turtle.listen()
    bind_keyboard_characters()
    refresh_screen()

# --- INTERACTIVE KEYBOARD TERMINAL REGISTRY HOOKS ---

def process_key_stroke(char):
    global current_string, input_mode
    if input_mode in ["angle", "force"]:
        if char.isdigit() or (char == '.' and '.' not in current_string):
            if len(current_string) < 6:
                current_string += char
                refresh_screen()
    elif input_mode in ["victory", "gameover"]:
        if char.lower() in ['y', 'n']:
            current_string = char.upper()
            refresh_screen()

def trigger_backspace():
    global current_string, input_mode
    if input_mode in ["angle", "force", "victory", "gameover"] and len(current_string) > 0:
        current_string = current_string[:-1]
        refresh_screen()

def trigger_enter_action():
    global current_string, input_mode, saved_angle, saved_force, feedback_msg, feedback_color
    
    if current_string == "":
        return
        
    if input_mode == "angle":
        try:
            val = float(current_string)
            if 0 <= val <= 360:
                saved_angle = val
                input_mode = "force"
                current_string = ""
                feedback_msg = f"AZIMUTH SECURED AT {saved_angle:.1f}°. COMPUTE THRUST RANGE PATTERNS..."
                feedback_color = "spring green"
            else:
                feedback_msg = "OUT OF RANGE ALERT. INPUT HEADING MUST BE 0-360 DEGREES."
                feedback_color = "red"
                current_string = ""
        except ValueError:
            current_string = ""
            
    elif input_mode == "force":
        try:
            val = float(current_string)
            if 1 <= val <= 10:
                saved_force = val
                current_string = ""
                simulate_tactical_artillery_fire()
            else:
                feedback_msg = "OUT OF VELOCITY BOUNDS. VELOCITY FACTOR MUST BE 1-10 VALUE."
                feedback_color = "red"
                current_string = ""
        except ValueError:
            current_string = ""
            
    elif input_mode in ["victory", "gameover"]:
        choice = current_string.upper()
        current_string = ""
        if choice == "Y":
            input_mode = "angle"
            feedback_msg = "DEPLOYING INCOMING RADAR PARALLEL VECTOR GRID MATRIX..."
            feedback_color = "spring green"
            init_new_polar_target()
        else:
            turtle.bye() # Safely disconnect and close terminal graphics cleanly
            return
            
    refresh_screen()

def trigger_space_action():
    global input_mode, feedback_msg, feedback_color, ammo
    if input_mode == "wait":
        if ammo <= 0:
            input_mode = "gameover"
            feedback_msg = "CRITICAL FAILURE: WEAPONS DEPLETED. COMMAND INTERACTION MANDATORY."
            feedback_color = "red"
            refresh_screen()
            return
        input_mode = "angle"
        feedback_msg = "TELEMETRY RESET. SCANNING RADAR GRID SENSORS FOR SOLUTION PATH..."
        feedback_color = "spring green"
        refresh_screen()

def simulate_tactical_artillery_fire():
    """Animates projectile deployment vector lines based on standard real-world mechanics."""
    global input_mode, ammo, last_angle, last_force
    FORCE_FACTOR = 30
    
    ammo -= 1
    last_angle = saved_angle
    last_force = saved_force
    
    turtle.goto(0, 0)
    turtle.setheading(saved_angle)
    turtle.hideturtle()
    turtle.pendown()
    
    distance = saved_force * FORCE_FACTOR
    turtle.tracer(1) 
    turtle.pencolor('#ff3333') 
    turtle.pensize(2)
    turtle.forward(distance)
    turtle.dot(10, '#ff3333') 
    turtle.penup()
    turtle.pensize(1)
    turtle.hideturtle()
    
    hit_x, hit_y = turtle.xcor(), turtle.ycor()
    check_polar_telemetry_hit(hit_x, hit_y)

def check_polar_telemetry_hit(hit_x, hit_y):
    """Processes precision targeting checks using true polar distance hypotenuse vectors."""
    global score, feedback_msg, feedback_color, input_mode
    
    shot_bearing = math.degrees(math.atan2(hit_y, hit_x)) % 360
    shot_range = math.sqrt(hit_x**2 + hit_y**2)
    
    distance_error = math.sqrt((hit_x - (target_x + 12.5))**2 + (hit_y - (target_y + 12.5))**2)
    
    # 1. Direct Target Lock Solution (Bullseye Center Hit within a 5-unit tolerance radius)
    if distance_error <= 5.0:
        score += 500
        input_mode = "victory"
        feedback_msg = f"🟢 BOOM! BULLSEYE DETONATION! (+500 XP) Verified Heading: {shot_bearing:.1f}°"
        feedback_color = "spring green"
        
    # 2. Proximity Scraping Hull Clip (Indirect Box Hit)
    elif target_x <= hit_x <= (target_x + 25) and target_y <= hit_y <= (target_y + 25):
        score += 50 
        angle_err = target_bearing - saved_angle
        force_err = (target_range / 30.0) - saved_force
        input_mode = "wait"
        
        feedback_msg = f"⚠️ PROXIMITY FLARE! (+50 XP) Azimuth: {angle_err:+.1f}° | Range: {force_err:+.2f} Mach"
        feedback_color = "orange"

    # 3. Open Canvas Miss
    else:
        angle_err = target_bearing - saved_angle
        force_err = (target_range / 30.0) - saved_force
        input_mode = "wait"
        
        steer_dir = "STEER RIGHT ➡️" if angle_err > 0 else "STEER LEFT ⬅️"
        burn_dir = "INCREASE THROTTLE 🔺" if force_err > 0 else "DECREASE THROTTLE 🔻"
        
        feedback_msg = f"❌ TARGET MISS! Radar Telemetry Guide -> {steer_dir} ({abs(angle_err):.1f}°) | {burn_dir}"
        feedback_color = "red"

def bind_keyboard_characters():
    """Binds operational numeric strokes across event loops."""
    for num in "0123456789.ynYN":
        turtle.onkey(lambda n=num: process_key_stroke(n), num)
    turtle.onkey(trigger_backspace, "BackSpace")
    turtle.onkey(trigger_enter_action, "Return") 
    turtle.onkey(trigger_space_action, "space")