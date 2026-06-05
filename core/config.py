# core/config.py
import random

TARGET_SIZE = 25

# Randomize target within the upper radar view bounds
TARGET_X = float(random.randint(-250, 250))
TARGET_Y = float(random.randint(0, 250))

BULLSEYE_X = TARGET_X + (TARGET_SIZE / 2)
BULLSEYE_Y = TARGET_Y + (TARGET_SIZE / 2)

shot_count = 0

# 🎮 NEW: Dedicated HUD User Inputs State Tracking
current_angle = 0.0
current_force = 5.0
is_fired = False # Traps controls while projectile is in flight

def increment_shots():
    global shot_count
    shot_count += 1