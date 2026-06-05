# TargetPractice/1play_me.py
import display
import title_animations
import game_play
import turtle

def main():
    # 1. Initialize screen frame context
    display.setup()
    
    # 2. Sequential Tutorial Sequences
    title_animations.sequence_1()
    title_animations.sequence_2()
    title_animations.sequence_3()
    
    # 3. Fire up interactive on-screen keyboard listener loops
    game_play.launch()
    
    # 🎯 THE PERMANENT CANVAS FIX:
    # Keeps the Python window completely locked open on macOS for input loops
    turtle.mainloop()

if __name__ == '__main__':
    main()
