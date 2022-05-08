from tkinter import *

import random

tk =Tk()

canvas = Canvas(tk, width=400, height=600)

tk.title("Space Invaders")

#canvas.pack()
canvas.pack(expand=YES, fill=BOTH)

# Load the .gif image file.
#bg = tk.PhotoImage(file='bg.gif')

# Put gif image on canvas.
# Pic's upper-left corner (NW) on the canvas is at x=50 y=10.
#canvas.create_image(50, 10, image=bg, anchor=NW)

canvas.create_rectangle(185, 570, 215, 600, fill="white", outline="red")

canvas.create_rectangle(35, 0, 65, 30, fill="red", outline="black")

canvas.create_rectangle(135, 0, 165, 30, fill="red", outline="black")
                        
canvas.create_rectangle(235, 0, 265, 30, fill="red", outline="black")

canvas.create_rectangle(335, 0, 365, 30, fill="red", outline="black")

canvas.configure(bg='black')