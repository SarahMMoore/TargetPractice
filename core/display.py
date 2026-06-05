# TargetPractice/core/display.py
import turtle
from core import physics

def setup():
    turtle.setup(600, 600)
    turtle.hideturtle()
    turtle.bgcolor('black')
    turtle.penup()

def draw_dashboard_hud(score, ammo, input_mode, current_string, feedback_msg, feedback_color):
    turtle.penup()
    turtle.goto(-300, -140)
    turtle.pencolor('#00ff66')
    turtle.pensize(2)
    turtle.pendown()
    turtle.goto(300, -140)
    turtle.penup()
    turtle.pensize(1)
    
    # Tally metrics draw
    turtle.goto(-270, -165)
    turtle.pencolor('white')
    turtle.write(f"📊 SYSTEM SCORE: {score} XP", font=("Courier", 11, "bold"))
    
    turtle.goto(80, -165)
    turtle.write(f"🔋 ORDNANCE CAPACITY: [{'█'*ammo}{'░'*(5-ammo)}]", font=("Courier", 11, "bold"))
    
    # History Memory draw
    turtle.goto(-270, -195)
    turtle.pencolor('silver')
    if physics.last_angle == "NONE":
        txt = "📟 SHOT TELEMETRY HISTORY >> [ NO PRIOR ORDNANCE DEPLOYED ]"
    else:
        txt = f"📟 LAST SHOT RECORDED  >> ANGLE: {physics.last_angle:.1f}°  |  FORCE: {physics.last_force:.2f} Mach"
    turtle.write(txt, font=("Courier", 10, "bold"))
    
    # Commands text mapping routing
    turtle.goto(-270, -225)
    turtle.pencolor('#00ff66')
    if input_mode == "angle":
        prompt = f"⚙️ RADAR DESK >> Input Launch Azimuth (Bearing 0-360°): {current_string}_"
    elif input_mode == "force":
        prompt = f"⚙️ RADAR DESK >> Input Terminal Velocity (Thrust Range 1-10): {current_string}_"
    elif input_mode == "victory":
        prompt = f"🎯 TARGET SOLVED! Engage another target coordinate blueprint? [Y/N]: {current_string}_"
    elif input_mode == "gameover":
        prompt = f"🚨 OUT OF AMMO! Restart [Y], Close [N], or Buy 5 rounds for 100 XP [C]: {current_string}_"
    else:
        prompt = "📡 VECTOR LOCKED >> Press [SPACEBAR] to recalibrate telemetry lines."
    turtle.write(prompt, font=("Courier", 10, "bold"))
    
    # Status Row feedback
    turtle.goto(-270, -255)
    turtle.pencolor(feedback_color)
    turtle.write(f">> {feedback_msg}", font=("Courier", 10, "bold"))
