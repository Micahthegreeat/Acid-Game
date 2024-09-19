import tkinter as tk
import turtle as tu
from PIL import Image
import os

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

t = tu.RawTurtle(canvas)

t.penup()
t.goto(-200, -175)
t.pendown()
draw_sierpinski(400, 1)
t.hideturtle()

canvas = tu.getcanvas()
psFilename = "foo.ps"
canvas.postscript(file=psFilename)
psimage = Image.open(psFilename)
psimage.save("bar.png") # or any other image format that PIL supports.
os.remove(psFilename) # optional