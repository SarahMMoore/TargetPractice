# TargetPractice/page_2.py
import turtle
import time

def show_tutorial():
    turtle.clear()
    turtle.pencolor('silver')
    
    # Render static blocks
    write_text(0, 250, 'TRY TO HIT THE TARGET', "times new roman", 20, "bold", "center")
    write_text(-275, 200, 'TO PLAY:', "times new roman", 20, "normal", "left")
    write_text(-200, 125, '~ When prompted, enter the angle and force \n\tof your projectile.', "times new roman", 16, "italic", "left")
    write_text(-200, 75, '~ Hitting anywhere within the square damages \n\tthe target, but will not destroy it.', "times new roman", 16, "italic", "left")
    write_text(-200, 25, '~ To destroy the target, you must hit the \n\tcenter of the square.', "times new roman", 16, "italic", "left")
    
    turtle.update()
    time.sleep(4.5) # Clean delay instead of heavy turtle circles
    turtle.clear()

def write_text(x, y, text, font_name, size, style, alignment):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(text, align=alignment, font=(font_name, size, style))
    turtle.penup()
