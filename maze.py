from tkinter import *
import random

#create instance of tk
tk = Tk()

#We make a canvas that we can draw on
canvas = Canvas(tk, width=500, height=500)

#Set the title of the window
tk.title("Maze")

#create the window and show it up on the screen
canvas.pack()

#create lines to draw a maze
canvas.create_line(100, 100, 500, 100)
canvas.create_line(0, 200, 200, 200)
canvas.create_line(300, 100, 300, 300)
canvas.create_line(400, 200, 400, 400)
canvas.create_line(400, 200, 400, 300)
canvas.create_line(100, 300, 100, 400)
canvas.create_line(200, 300, 200, 400)
canvas.create_line(300, 400, 200, 400)
canvas.create_line(300, 100, 400, 100)
canvas.create_line(0, 400, 100, 400)