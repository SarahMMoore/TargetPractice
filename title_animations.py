import page_1
import page_2
import page_3
import turtle

def main():
    sequence_1()
    sequence_2()
    sequence_3()

def sequence_1():
    page_1.line_1()
    page_1.x_axis.setup()
    page_1.x_axis.draw_line.draw()
    page_1.line_2()
    page_1.y_axis.setup()
    page_1.y_axis.draw_line.draw()
    page_1.quadrant.draw()
    turtle.reset()
    turtle.hideturtle()
    
def sequence_2():
    page_2.line_1()
    page_2.line_2()
    page_2.line_3()
    page_2.line_4()
    page_2.line_5()
    page_2.pause()

def sequence_3():
    page_3.line()
    page_3.pause()

if __name__ == '__main__': 
    main()
