# Sarah Moore
# Programming Assignment 4
# CS 250
# 08. October 2024
# Game that asks user for input and loops until
# the users input matches a specific data set.
# Target Practice

import display
import title_animations
import game_play
import turtle

def main():
    
    display.setup()
    title_animations.sequence_1()
    title_animations.sequence_2()
    title_animations.sequence_3()
    game_play.launch() 

if __name__ == '__main__':
    main()

