import turtle
from . import x_axis
from . import y_axis
from . import quadrant

def main():
    x_axis.setup()
    x_axis.draw_line.draw()
    y_axis.setup()
    y_axis.draw_line.draw()
    quadrant.draw()

if __name__ == '__main__': 
    main()

