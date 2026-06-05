# TargetPractice/core/physics.py
import turtle
import math
import time

target_bearing = 0.0
target_range = 0.0
historical_shot_vectors = []
last_angle = "NONE"
last_force = "NONE"

def calculate_target_solution(t_x, t_y):
    global target_bearing, target_range
    b_x = t_x + 12.5
    b_y = t_y + 12.5
    
    # Calculate tracking vectors relative to (0, 80)
    target_bearing = math.degrees(math.atan2(b_y - 80, b_x)) % 360
    target_range = math.sqrt(b_x**2 + (b_y - 80)**2)

def draw_historical_trails():
    for shot in historical_shot_vectors:
        turtle.goto(0, 80)
        turtle.setheading(shot['angle'])
        turtle.pencolor(shot['color'])
        turtle.pendown()
        turtle.forward(shot['force'] * 30)
        turtle.dot(6, shot['color'])
        turtle.penup()

def animate_victory_flash():
    """🎯 NEW: Disconnects the screen matrix and flashes an alarm banner."""
    turtle.tracer(0)
    
    # Run a high-speed arcade-style flashing cycle 3 times
    for _ in range(3):
        # Frame A: Alert Red Canvas
        turtle.clear()
        turtle.bgcolor('#7f2626')
        turtle.pencolor('black')
        turtle.goto(0, 40)
        turtle.write('💥 DIRECT HIT!! 💥', align="center", font=("elephant", 28, "bold"))
        turtle.goto(0, -20)
        turtle.write('TARGET COMPLETELY ANNIHILATED', align="center", font=("Courier", 14, "bold"))
        turtle.update()
        time.sleep(0.25)
        
        # Frame B: Terminal Green Canvas
        turtle.clear()
        turtle.bgcolor('#0b130e')
        turtle.pencolor('#00ff66')
        turtle.goto(0, 40)
        turtle.write('💥 DIRECT HIT!! 💥', align="center", font=("elephant", 28, "bold"))
        turtle.goto(0, -20)
        turtle.write('TARGET COMPLETELY ANNIHILATED', align="center", font=("Courier", 14, "bold"))
        turtle.update()
        time.sleep(0.25)

def simulate_shot(angle, force, t_x, t_y):
    global last_angle, last_force
    last_angle, last_force = angle, force
    
    # Deploy projectile from (0, 80)
    turtle.goto(0, 80)
    turtle.setheading(angle)
    turtle.pendown()
    turtle.pencolor('white')
    turtle.pensize(2)
    
    distance = force * 30
    turtle.tracer(1)
    turtle.forward(distance)
    turtle.dot(10, 'white')
    turtle.penup()
    turtle.pensize(1)
    turtle.hideturtle()
    
    hit_x, hit_y = turtle.xcor(), turtle.ycor()
    
    # Telemetry math relative to (0, 80)
    shot_bearing = math.degrees(math.atan2(hit_y - 80, hit_x)) % 360
    shot_range = math.sqrt(hit_x**2 + (hit_y - 80)**2)
    
    b_x, b_y = t_x + 12.5, t_y + 12.5
    distance_error = math.sqrt((hit_x - b_x)**2 + (hit_y - b_y)**2)
    
    if distance_error <= 5.0:
        # 🎯 NEW: Intercept code execution to trigger the cinematic flashing splash card first!
        animate_victory_flash()
        
        # Returns cleanly to main layout loop screen and engages play again prompts
        return True, f"🟢 BULLSEYE DETONATION! (+500 XP) Heading: {shot_bearing:.1f}°", "spring green", 500
        
    elif t_x <= hit_x <= (t_x + 25) and t_y <= hit_y <= (t_y + 25):
        historical_shot_vectors.append({'angle': angle, 'force': force, 'color': '#cca300'})
        angle_err = target_bearing - angle
        force_err = (target_range / 30.0) - force
        return False, f"⚠️ PROXIMITY FLARE! (+50 XP) Azimuth: {angle_err:+.1f}° | Range: {force_err:+.2f}", "orange", 50
    else:
        historical_shot_vectors.append({'angle': angle, 'force': force, 'color': '#7f2626'})
        angle_err = target_bearing - angle
        force_err = (target_range / 30.0) - force
        steer_dir = "STEER RIGHT ➡️" if angle_err > 0 else "STEER LEFT ⬅️"
        burn_dir = "INCREASE THROTTLE 🔺" if force_err > 0 else "DECREASE THROTTLE 🔻"
        return False, f"❌ TARGET MISS! Guide -> {steer_dir} ({abs(angle_err):.1f}°) | {burn_dir}", "red", 0
