# 1play_me.py
# Sarah Moore # Programming Assignment 4 # CS 250 # 08. October 2024 

from graphics import display
from scenes import title_animations
import turtle 

def main():
    display.setup()
    # Launch the interactive menu page sequence
    title_animations.start_menu()
    # Keep the system window open and listening for keyboard presses
    turtle.mainloop()

if __name__ == '__main__':
    main()
