import tkinter as tk
from PIL import ImageGrab
from PIL import Image
import turtle
import time


def dump_gui():
    """
    takes a png screenshot of a tkinter window, and saves it on in cwd
    """
    print('...dumping gui window to png')
    
    
    #my screen in defaultly scaled up to 150 percent in windows

    x0 = root.winfo_rootx() * 1.5 + 6
    y0 = root.winfo_rooty() * 1.5 + 8
    x1 = x0 + root.winfo_width() * 1.5 - 10
    y1 = y0 + root.winfo_height() * 1.5 - 12
    ImageGrab.grab().crop((x0, y0, x1, y1)).save("gui_image_grabbed.png")
    image = Image.open('gui_image_grabbed.png')
    new_image = image.resize((16, 16))
    new_image.save('gui_image_grabbed.png')


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


def pixelDraw(x, y, color):
    x = x -8
    y = y-8
    x = x * 40
    y = y * 40
    canvas.create_rectangle( (x, y),(x+39, y + 39), outline=color, fill =color)

root = tk.Tk()
canvas = tk.Canvas(root, width=640, height=640)
canvas.pack()

t = turtle.RawTurtle(canvas)

for i in range(0,16):
    for c in range(0,16):\
        pixelDraw(i,c,"#000000")
for i in range(4, 13):
    pixelDraw(i,0, 'green')
for i in range(3, 14):
    pixelDraw(i,1, 'green')
pixelDraw(3,2, 'green')
pixelDraw(13,2, 'green')




t.hideturtle()
#input()

dump_gui()
print('checking up')
#root.mainloop()