# TargetPractice/1play_me.py
from core import display, game_display
from interface import manager
import turtle

def main():
    # 1. Initialize screen frame context
    display.setup()
    
    # 2. Sequential Tutorial Sequences from our interface package
    manager.run_sequences()
    
    # 3. Fire up interactive on-screen keyboard listener loops from our engine pack
    game_display.launch()
    
    # Keeps window locked open safely on macOS
    turtle.mainloop()

if __name__ == '__main__':
    main()
