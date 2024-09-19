import tkinter as tk
from PIL import ImageGrab
import turtle
import time


def dump_gui():
    """
    takes a png screenshot of a tkinter window, and saves it on in cwd
    """
    print('...dumping gui window to png')
    root.update()
    

    x0 = root.winfo_rootx() * 2
    y0 = root.winfo_rooty() * 2
    x1 = x0 + (root.winfo_width() * 2) 
    y1 = y0 + (root.winfo_height() *2)
    ImageGrab.grab().crop((x0, y0, x1, y1)).save("gui_image_grabbed.png")


def draw_sierpinski(length, depth):
    if depth == 0:
        for i in range(0, 3):
            t.fd(length)
            t.left(120)
    else:
        draw_sierpinski(length / 2, depth - 1)
        t.fd(length / 2)
        draw_sierpinski(length / 2, depth - 1)
        t.bk(length / 2)
        t.left(60)
        t.fd(length / 2)
        t.right(60)
        draw_sierpinski(length / 2, depth - 1)
        t.left(60)
        t.bk(length / 2)
        t.right(60)


root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

t = turtle.RawTurtle(canvas)

t.penup()
t.goto(-200, -175)
t.pendown()
draw_sierpinski(400, 1)



t.hideturtle()

dump_gui()
print('checking up')
#root.mainloop()